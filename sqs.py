import boto3

client = boto3.client('sqs')

def start():
    return client

def create_q(queue_name):
    '''give name get queue'''
    response = client.create_queue(QueueName='producer')
    queue_url = response['QueueUrl']
    return response, queue_url

def delete_q(queue_name):
    '''give name delete queue'''
    response = client.delete_queue(QueueName='producer')
    queue_url = response['QueueUrl']
    return response, queue_url

def list_q():
    '''get list of all queues'''
    queues = client.list_queues()
    return queues['QueueUrls']

def q_name2url(queue_name):
    '''give name get url'''
    queue_url = client.get_queue_url(QueueName=queue_name)
    return queue_url['QueueUrl']

def send_msg(queue_name, message):
    '''gueue name + msg sent'''
    url = queue_url(client, queue_name)
    response = client.send_message(
        QueueUrl = url,
        MessageBody = message)
    status_code = response['ResponseMetadata']['HTTPStatusCode']
    return response, status_code

def receive_msg(queue_name):
    '''give name receive msgs'''
    url = queue_url(client, queue_name)
    response = client.receive_message(QueueUrl=url, MaxNumberOfMessages=10)
    return response

def delete_msg():
    '''ntg'''
    pass

def purge_q(queue_name):
    '''purge named queue'''
    url = queue_url(client, queue_name)
    response = client.purge_queue(QueueUrl=url)
    return response