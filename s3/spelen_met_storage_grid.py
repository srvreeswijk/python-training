from storage_grid import StorageGrid

s3_endpoint = "https://osg.gn2.rijkscloud.nl/"
profile     = 'rijkszaak'
bucket      = 'prod4-demo-acc01-db-archive'

sg = StorageGrid(s3_endpoint, profile)
sg.set_max_items(6000)

# sg.list_buckets()
sg.list_objects(bucket)