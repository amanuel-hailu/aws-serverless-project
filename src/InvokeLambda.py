import boto3
import json

def lambda_handler(event, context):
    lambdaCode = boto3.client("lambda", region_name='us-east-1')

    payload = {"message": "Hi, you have been invoked."}
    response = lambdaCode.invoke(FunctionName = "HelloLambdaDemo",
    InvocationType = "RequestResponse",
    Payload = json.dumps(payload))

    print(response["Payload"].read())

    return 'Hello from lambda'
