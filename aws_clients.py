import boto3
import config

session = boto3.Session(profile_name=config.profile_name)

kinesis_client = session.client("kinesis")
dynamo_resource = session.resource("dynamodb")

