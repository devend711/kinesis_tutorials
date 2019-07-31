import aws_clients
import time
import config
import json

kinesis_client = aws_clients.kinesis_client
shard_id = "shardId-000000000000" #only one shard
shard_iterator = kinesis_client.get_shard_iterator(StreamName=config.kinesis_stream_name, ShardId=shard_id, ShardIteratorType="LATEST")["ShardIterator"]

dynamodb = aws_clients.dynamo_resource
table = dynamodb.Table(config.dynamo_table_name)

print("Ready to watch Kinesis stream " + config.kinesis_stream_name + ", shard " + shard_id)

while True:
    out = kinesis_client.get_records(ShardIterator=shard_iterator, Limit=100)
    for record in out["Records"]:
        print("Record arrived at ~" + record["ApproximateArrivalTimestamp"].strftime("%Y-%m-%d %H:%M:%S"))
        tweet_json = json.loads(record["Data"])
        print(tweet_json)
        response = table.put_item(
            Item={
                "username": tweet_json["username"],
                "timestamp": tweet_json["timestamp"],
                "message": tweet_json["message"]
            }
        )
    shard_iterator = out["NextShardIterator"]
    time.sleep(1.0)
