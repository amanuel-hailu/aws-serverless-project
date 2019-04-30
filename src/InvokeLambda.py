import boto3
import json

def lambda_handler(event, context):
    lambdaCode = boto3.client("lambda", region_name='us-east-1')

    payload = {"message": "Hello"}

    response = lambdaCode.invoke(FunctionName = "HelloLambda",
                InvocationType = "RequestResponse",
                Payload = json.dumps(payload))

    x = response["Payload"].read()
    
    return eval(x)
