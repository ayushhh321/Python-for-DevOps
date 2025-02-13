# we use boto3 when we have to use python with aws
# first we have to configure local machine to aws using iam and aws cli 

import boto3

s3=boto3.resources("s3") #boto3 ko bol rha hu baki sare services chor ke only s3 pr dhyan do

def show_buckets(s3):
  # print(buckets.name.all()) it will print all the bucket but in collecion format
    for bucket in s3.buckets.all():
      print(bucket.name)
    
def create_bucket(s3):
  s3.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint': region })  #from documentation code copy pasted
  
  print("bucket created")
  
 
#jo backup create kra toh now upplaoding to s3 
def upload_backup(s3, file_name, bucket_name, key_name):

  data = open(file_name, 'rb") # file gets read in binary me read hoga
  s3.Bucket(bucket_name).put_object(Key=key_name) Body=data)
  print("Backup Uploaded successfully")

bucket_name = "python-for-devops-junoon"
region = "us-east-2"
# create_bucket(s3,bucket_name, region)
# show_buckets(s3)
file_name = "D:\folders\Python for DevOps>"
upload_backup(s3, file_name,bucket_name,"my-backup.tar.gz")
  
  
