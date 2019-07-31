import aws_clients
import config
import json
TWEET_FILE_NAME='tweets.json'
kinesis_client = aws_clients.kinesis_client

with open(TWEET_FILE_NAME) as json_data:
    data = json.load(json_data)
    print(data)
    for tweet in data:
        kinesis_client.put_record(StreamName=config.kinesis_stream_name, Data=json.dumps(tweet), PartitionKey=tweet["username"])
