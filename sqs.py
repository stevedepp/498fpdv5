def sqs_start():
    import boto3
    client = boto3.client('sqs')
    return client

def sqs_create_queue(client, queue_name):
    response = client.create_queue(QueueName='producer')
    queue_url = response['QueueUrl']
    return response, queue_url

def list_queues(client):
    queues = client.list_queues()
    return queues['QueueUrls']

def queue_url(client, queue_name):
    queue_url = client.get_queue_url(QueueName=queue_name)
    return queue_url['QueueUrl']

def sqs_send_msg(client, queue_name, message):
    url = queue_url(client, queue_name)
    response = client.send_message(
        QueueUrl = url,
        MessageBody = message)
    status_code = response['ResponseMetadata']['HTTPStatusCode']
    return response, status_code

def sqs_receive_msg(client, queue_name):
    url = queue_url(client, queue_name)
    response = client.receive_message(QueueUrl=url, MaxNumberOfMessages=10)
    return response

def sqs_delete_msg():
    pass

def sqs_purge_queue(client, queue_name):
    url = queue_url(client, queue_name)
    response = client.purge_queue(QueueUrl=url)
    return response