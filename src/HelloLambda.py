def lambda_handler(event, context):
    print(event)
    response = {
        "statusCode": 200,
        "body": "Hello, this is Amanuel!!!"
    }
    return response
