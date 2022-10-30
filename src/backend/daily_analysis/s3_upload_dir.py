import logging
import boto3
from botocore.exceptions import ClientError
import os


# https://stackoverflow.com/questions/25380774/upload-a-directory-to-s3-with-boto

# used to upload folders to S3




def uploadDirectory(path,bucketname):
        for root,dirs,files in os.walk(path):
            for file in files:
                s3.upload_file(os.path.join(root,file),bucketname,file)