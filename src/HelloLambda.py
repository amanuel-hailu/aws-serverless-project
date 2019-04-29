def lambda_handler(event, context):
    print(event)
    response = {
        "statusCode": 200,
        "body": "Hello, this is HelloLambda!!!"
    }
    return response
