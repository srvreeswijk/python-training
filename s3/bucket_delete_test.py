import os
import boto3
import time

from storage_grid import StorageGrid

fileCount = 0
generated_number_of_files = 3000
page_size = 500

s3_endpoint = "https://osg.gn2.rijkscloud.nl/"
profile     = 'rijkszaak'


sg = StorageGrid(s3_endpoint, profile)
sg.set_page_size(page_size)

print("Starting test with generated number of files: ", generated_number_of_files)

# Create a bucket
bucket      = 'sbx4-bas-deletion-test-bucket'
sg.create_bucket(bucket)

# Create a bucket full of files
begin_time = time.time()
for i in range(generated_number_of_files):
    # get random string of 5 characters 
    random_string = os.urandom(5).hex()
    print('Uploading file number [%d]\r'%i, end="")
    object_name = f's3/lore_ipsum_{random_string}_{i}.txt'
    sg.upload_file(bucket, 's3/lore_ipsum.txt', object_name)

end_time = time.time()
time_elapsed = int(end_time - begin_time)
print(f"Time to upload {generated_number_of_files} files: {time_elapsed}s")

# Let storege grid catch up
print("Let storage grid catch up")
time.sleep(1)

def delete_all_normal():
    # delete all objects in test bucket
    begin_time = time.time()
    # sg.delete_all_objects(bucket)
    sg.delete_all_objects_in_bucket(bucket)
    end_time = time.time()
    time_elapsed = int(end_time - begin_time)
    print(f"Time to delete all objects in bucket {bucket}: {time_elapsed}s")

# delete_all_normal()

def delete_all_threaded():
    # delete all objects in test bucket
    begin_time = time.time()
    sg.delete_all_objects_in_bucket_threaded(bucket)
    end_time = time.time()
    time_elapsed = int(end_time - begin_time)
    print(f"Time to delete all objects in bucket {bucket}: {time_elapsed}s")


# delete_all_normal()
delete_all_threaded()

# Het deleten testen met de storagegrid bash scripts kan je doen door:
# time ./remove-bucket.sh sbx4-bas-deletion-test-bucket rijkszaak
# Als het goed is gebruikt hij het rijkszaak profiel uit je aws credentials file
# Zo niet, dan moet je even de init.sh file source-en, en hier de juiste credentials invullen. 
# source init.sh