import boto3
import json

def lambda_handler(event, context):
    lambdaCode = boto3.client("lambda", region_name='us-east-1')

    payload = {"message": "I am Amanuel"}

    response = lambdaCode.invoke(FunctionName = "HelloLambda",
    InvocationType = "RequestResponse",
    Payload = json.dumps(payload))

    x = response["Payload"].read()
    print(x)

    # y = {
    #     "statusCode": 200,
    #     "body": "This is Prince"
    # }


    return eval(x)
