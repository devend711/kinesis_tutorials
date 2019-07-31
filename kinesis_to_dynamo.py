import boto3
import aws_clients
import time
import json
import decimal
import config

kinesis_client = aws_clients.kinesis_client
shard_id = 'shardId-000000000000' #only one shard
shard_iterator = kinesis_client.get_shard_iterator(StreamName=config.kinesis_stream_name, ShardId=shard_id, ShardIteratorType="LATEST")["ShardIterator"]

dynamodb = aws_clients.dynamo_resource
table = dynamodb.Table(config.dynamo_table_name)

while True:
    out = kinesis_client.get_records(ShardIterator=shard_iterator, Limit=100)
    for record in out['Records']:
        print("Record arrived at ~" + record['ApproximateArrivalTimestamp'].strftime("%Y-%m-%d %H:%M:%S"))
    shard_iterator = out["NextShardIterator"]
    time.sleep(1.0)
