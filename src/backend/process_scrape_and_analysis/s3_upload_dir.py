# code from https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
# https://stackoverflow.com/questions/25380774/upload-a-directory-to-s3-with-boto

import logging
import boto3
from botocore.exceptions import ClientError
import os


# upload_file(file_name, bucket, object_name=None)

# if csv is already open use this one
#
# s3 = boto3.client('s3')
# with open("FILE_NAME", "rb") as f:
#     s3.upload_fileobj(f, "BUCKET_NAME", "OBJECT_NAME")


def uploadDirectory(path,bucketname):
        for root,dirs,files in os.walk(path):
            for file in files:
                s3C.upload_file(os.path.join(root,file),bucketname,file)