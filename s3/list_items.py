import boto3
from boto3 import Session

s3_endpoint = "https://osg.gn2.rijkscloud.nl/"
# s3_bucket = 'prod4-demo-tst03-acs-hot'
# bucket = 'prod4-demo-tst03-db-archive'


def list_objects(bucket_name):
    
    session = boto3.Session(profile_name='rijkszaak')
    s3 = session.client('s3', endpoint_url=s3_endpoint)

    paginator = s3.get_paginator('list_objects')
    #response_iterator = paginator.paginate(Bucket=bucket)
    response_iterator = paginator.paginate( Bucket=bucket_name, 
                                            PaginationConfig={
                                                "MaxItems": 10,
                                                "PageSize": 50, 
                                                "StartingToken": None,
                                            }
    )

    # for page in response_iterator:
    #     print(page)

    buckets_found = False
    for page in response_iterator:
        if "Contents" in page and page["Contents"]:
            buckets_found = True
            for bucket in page["Contents"]:
                print(f"\t{bucket['Key']}")
        
    if not buckets_found:
        print("No buckets found!")

if __name__ == "__main__":
    list_objects('prod4-demo-tst03-acs-hot')