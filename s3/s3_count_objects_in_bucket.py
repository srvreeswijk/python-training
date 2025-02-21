import boto3
import time

from storage_grid import StorageGrid

"""Simple module to count the amount of files in a bucket"""

fileCount = 0

s3_endpoint = "https://osg.gn2.rijkscloud.nl/"
profile     = 'rijkszaak'
bucket      = 'prod4-bsd-tst01-acs-hot'

sg = StorageGrid(s3_endpoint, profile)
s3 = sg.s3

# print header
print("{:<50}: {:<10}: {:<10}".format('bucket', 'fileCount', 'time (s)'))

def amount_of_files_in_bucket(bucket) -> tuple[int, int]:
    """List all the object in a specific bucket"""
    fileCount = 0
    begin_time = time.time()
    s3p = s3.get_paginator('list_objects_v2')
    s3i = s3p.paginate(Bucket=bucket)
    for KeyCount in s3i.search('KeyCount'):
      fileCount += KeyCount
    end_time = time.time()
    time_elapsed = int(end_time - begin_time)
    return fileCount, time_elapsed


for bucket in sg.list_buckets():
    """Loop over all buckets and print the amount of files in each bucket"""
    fileCount, time_elapsed = amount_of_files_in_bucket(bucket)
    print("{:<50}: {:<10}: {:<10}".format(bucket, fileCount, time_elapsed))


# begin_time = time.time()
# fileCount = amount_of_files_in_bucket(bucket)
# end_time = time.time()
# time_elapsed = int(end_time - begin_time)
# print("{:<50}: {:<10}: {:<10}s".format(bucket, fileCount, time_elapsed))