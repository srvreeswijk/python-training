import boto3

from storage_grid import StorageGrid

fileCount = 0

s3_endpoint = "https://osg.gn2.rijkscloud.nl/"
profile     = 'rijkszaak'
bucket      = 'prod4-demo-acc01-db-archive'

sg = StorageGrid(s3_endpoint, profile)
s3 = sg.s3

[print(bucket) for bucket in sg.list_buckets()]