import boto3
import json

S3API = boto3.client("s3", region_name="us-east-1") 
bucket_name = "c103192a2383148l7438580t1w117912221617-s3bucket-cnbvhj6y1l23"

policy_file = open("/home/ec2-user/environment/resources/public_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("Setting Permissions - DONE")