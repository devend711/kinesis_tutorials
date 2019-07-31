import aws_clients
import config
import time

kinesis_client = aws_clients.kinesis_client
shard_id = "shardId-000000000000" #only one shard!

pre_shard_iterator = kinesis_client.get_shard_iterator(StreamName=config.kinesis_stream_name, ShardId=shard_id, ShardIteratorType="LATEST")
shard_iterator = pre_shard_iterator["ShardIterator"]

# Print out any records from the shard
while True:
    out = kinesis_client.get_records(ShardIterator=shard_iterator, Limit=1)
    shard_iterator = out["NextShardIterator"]
    print out['Records']
    time.sleep(1.0)
