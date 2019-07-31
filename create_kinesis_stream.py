import aws_clients
import config

response = aws_clients.kinesis_client.create_stream(
   StreamName=config.kinesis_stream_name,
   ShardCount=1
)
