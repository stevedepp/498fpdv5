response = client.create_table(
    AttributeDefinitions=[
    {
        'AttributeName': 'name',
        'AttributeType': 'S'
    }
    ],
    TableName='producer',
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