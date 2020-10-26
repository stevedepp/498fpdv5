

import boto3

def delete(name):
    client = boto3.client('s3')

    response = client.delete_bucket(
        Bucket='aws-sam-cli-managed-default-samclisourcebucket-g8yh0dei4jqb')