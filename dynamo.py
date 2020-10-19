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

table_name = 'producer'

request_type = 'PutRequest'

def dynamo_table(name):

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

def dynamo_items(name):
    response = client.batch_write_item(
    RequestItems={
        name: put_request
        }
        )

def dynamo_delete(name):
    response = client.delete_table(TableName=name)


def request(request_type, company_names):
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

