import time
import boto3
from boto3 import Session
import typing
import threading

class StorageGrid():

    s3_endpoint = ''
    aws_profile = ''
    pagination_config = {
                "PageSize": 500, 
                "StartingToken": None,
            }
    s3 = None

    def __init__(self, s3_endpoint, aws_profile='rijkszaak'):
        self.s3_endpoint = s3_endpoint
        self.aws_profile = aws_profile
        session = boto3.Session(profile_name=self.aws_profile)
        self.s3 = session.client('s3', endpoint_url=self.s3_endpoint)
        self.cumulative_counter = 0
        self.lock = threading.Lock()

    def list_buckets(self) -> typing.List[str]:
        """List all the available buckets"""
        buckets = []

        paginator = self.s3.get_paginator('list_buckets')
        response_iterator = paginator.paginate(
            PaginationConfig=self.pagination_config
        )

        for page in response_iterator:
            if "Buckets" in page and page["Buckets"]:

                for bucket in page["Buckets"]:
                    buckets.append(bucket['Name'])
                    #print(f"\t{bucket['Name']}")

        return buckets

    def list_objects(self, bucket_name) -> list:
        """List all the object in a specific bucket"""
        
        session = boto3.Session(profile_name=self.aws_profile)
        s3 = session.client('s3', endpoint_url=self.s3_endpoint)

        paginator = self.s3.get_paginator('list_objects')
        #response_iterator = paginator.paginate(Bucket=bucket)
        response_iterator = paginator.paginate( Bucket=bucket_name, 
            PaginationConfig=self.pagination_config
        )

        object_list = []
        pages = 0
        for page in response_iterator:
            pages += 1
            if "Contents" in page and page["Contents"]:
                for bucket in page["Contents"]:
                    # print(f"\t{bucket['Key']}")
                    object_list.append([bucket['Key']])
        # print("Amount of pages: " + str(pages))
        return object_list
    
    def amount_of_files_in_bucket(self, bucket) -> tuple[int, int]:
        """List all the object in a specific bucket"""
        fileCount = 0
        begin_time = time.time()
        s3p = self.s3.get_paginator('list_objects_v2')
        s3i = s3p.paginate(Bucket=bucket)
        for KeyCount in s3i.search('KeyCount'):
            fileCount += KeyCount
        end_time = time.time()
        time_elapsed = int(end_time - begin_time)
        return fileCount, time_elapsed
    
    def delete_all_objects(self, bucket):
        """Delete all objects in a specific bucket"""
        bucket = self.s3.Bucket(bucket)
        # suggested by Jordon Philips 
        bucket.objects.all().delete()
    
    def delete_all_objects_in_bucket(self, bucket):
        """Delete all objects in a specific bucket"""
        begin_time = time.time()
        s3p = self.s3.get_paginator('list_objects_v2')
        s3i = s3p.paginate(Bucket=bucket)
        i = 0
        for Key in s3i.search('Contents'):
            i+=1
            # print('Deleting file number [%d]\r'%i, end="")
            if Key is not None:
                self.s3.delete_object(Bucket=bucket, Key=Key['Key'])
        end_time = time.time()
        time_elapsed = int(end_time - begin_time)
        return time_elapsed
    
    def delete_page(self, bucket, page):
       deleted_count = 0
       for file in page['Contents']:
            if file is not None:
                # time.sleep(0.2)
                self.s3.delete_object(Bucket=bucket, Key=file['Key'])
                deleted_count += 1
                # print each tenth file
                if deleted_count % 10 == 0:
                    print('Deleting file number [%d]\r'%self.cumulative_counter, end="")
       with self.lock:
            self.cumulative_counter += deleted_count
    
    def delete_all_objects_in_bucket_threaded(self, bucket):
        """Delete all objects in a specific bucket"""
        begin_time = time.time()
        s3p = self.s3.get_paginator('list_objects_v2')
        s3i = s3p.paginate(Bucket=bucket, PaginationConfig=self.pagination_config)
        threads = []
        for page in s3i:
            num_keys = page['KeyCount']
            if num_keys == 0:
                break
            # print("Page type: ", type(page))
            # print("Next Page...  isTruncated: {} ".format(page['IsTruncated']))
            threads.append(threading.Thread(target=self.delete_page, args=[bucket, page]))
            threads[-1].start()
            print("Starting thread: " + str(len(threads)) + " with " + str(num_keys) + " items")
        for thread in threads:
            thread.join()
        
        end_time = time.time()
        time_elapsed = int(end_time - begin_time)
        print(f"Total objects deleted: {self.cumulative_counter}")
        return time_elapsed


    def set_max_items(self, max: int):
        self.pagination_config['MaxItems'] = max

    def set_page_size(self, size: int):
        self.pagination_config['PageSize'] = size

    def create_bucket(self, bucket_name):
        """Create a new bucket"""
        self.s3.create_bucket(Bucket=bucket_name)
    
    def upload_file(self, bucket_name, file_name, object_name=None):
        """Upload a file to a bucket"""
        with open(file_name, "rb") as f:
            self.s3.upload_file(file_name, bucket_name, object_name)
        