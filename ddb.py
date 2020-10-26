company_names = [
    'facebook', 
    'amazon', 
    'netflix', 
    'google', 
    'microsoft', 
    'ibm', 
    'oracle', 
    'spotify', 
    'nvidia']

table_name = 'fang'

request_type = 'PutRequest'

import boto3
client = boto3.client('dynamodb')

def table_make(name=table_name):
    '''give name get created ddb table'''
    response = client.create_table(
        AttributeDefinitions=[
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        }
        ],
        TableName=name,
        KeySchema=[
        {
            'AttributeName': 'name',
            'KeyType':'HASH'
        },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        },
    )
    return response

def delete_table(name=table_name):
    '''delete a named dynamodb table'''
    response = client.delete_table(TableName=name)

def request(request_type=request_type, company_names=company_names):
    request_names = []
    for company_name in company_names:
        request_names.append(
            {request_type:
                {'Item':
                    {'name':
                        {'S': company_name}
                    }
                }
            }
        )
    return request_names

def add_items(name=table_name, request=request()):
    '''give ddb name and put items in it'''
    response = client.batch_write_item(
    RequestItems={
        name: request
        }
        )
    return response
