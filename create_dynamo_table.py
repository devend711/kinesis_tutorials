import aws_clients
import config

dynamodb = aws_clients.dynamo_resource
table_name = config.dynamo_table_name

table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'message',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'message',
            'AttributeType': 'S'
        }
    ],
    # pricing determined by ProvisionedThroughput
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
