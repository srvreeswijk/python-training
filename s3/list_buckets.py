import boto3

tenant_id = '11647502759062162786'
tenant_user = 'sa_deploy'
tenant_password = 'qYQo0ihIuEVyquZYO5F3TC7WsBo83Ef'
s3_endpoint = "https://osg.gn2.rijkscloud.nl/"

access_key = 'W13BBT8W69CXI03U2QV6'
secret_key = 'WPhX71wiNPWvKe258e05SdyQsHpcRw+i9ayXSjBW'

def list_buckets():
    
    s3 = boto3.client("s3", aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key,
                            endpoint_url=s3_endpoint
                            )

    paginator = s3.get_paginator('list_buckets')
    response_iterator = paginator.paginate(
        PaginationConfig={
            "PageSize": 50, 
            "StartingToken": None,
        }
    )

    buckets_found = False
    for page in response_iterator:
        if "Buckets" in page and page["Buckets"]:
            buckets_found = True
            for bucket in page["Buckets"]:
                print(f"\t{bucket['Name']}")
        
    if not buckets_found:
        print("No buckets found!")

if __name__ == "__main__":
    list_buckets()