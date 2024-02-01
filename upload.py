import logging
import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv

load_dotenv()

S3_BUCKET_NAME = os.environ["S3_BUCKET_NAME"]
S3_BUCKET_URL = os.environ["S3_BUCKET_URL"]
ACCESS_KEY_ID = os.environ["ACCESS_KEY_ID"]
SECRET_ACCESS_KEY = os.environ["SECRET_ACCESS_KEY"]

def upload_file(file_name, bucket = S3_BUCKET_NAME, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3',
                             aws_access_key_id=ACCESS_KEY_ID,
                             aws_secret_access_key=SECRET_ACCESS_KEY)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True