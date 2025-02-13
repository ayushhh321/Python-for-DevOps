# we use boto3 when we have to use python with aws
# first we have to configure local machine to aws using iam and aws cli 

import boto3

s3=boto3.resources("s3") #boto3 ko bol rha hu baki sare services chor ke only s3 pr dhyan do

def show_buckets(s3):
  # print(buckets.name.all()) it will print all the bucket but in collecion format
    for bucket in s3.buckets.all():
      print(bucket.name)
    
def create_bucket(s3):
  s3.create_bucket(Bucket="pyhton - ayush",CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})  #from documentation
  
  print("bucket created")
  
create_bucket(s3)
show_buckets(s3)