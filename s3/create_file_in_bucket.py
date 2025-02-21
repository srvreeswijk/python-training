import boto3
from botocore.exceptions import ClientError

class StorageGrid:
    def __init__(self, endpoint_url, profile_name):
        session = boto3.Session(profile_name=profile_name)
        self.s3 = session.client('s3', endpoint_url=endpoint_url)

    def upload_file(self, bucket_name, file_name, object_name):
        try:
            with open(file_name, 'rb') as file_data:
                self.s3.put_object(Bucket=bucket_name, Key=object_name, Body=file_data)
        except ClientError as e:
            print(f"Failed to upload {file_name} to {bucket_name}/{object_name}: {e}")

# Usage
s3_endpoint = "https://osg.gn2.rijkscloud.nl/"
profile = 'rijkszaak'
sg = StorageGrid(s3_endpoint, profile)

bucket = 'sbx4-bas-deletion-test-bucket'
# sg.create_bucket(bucket)

file_name = 's3/lore_ipsum.txt'
sg.upload_file(bucket, file_name, 'lore_ipsum.txt')