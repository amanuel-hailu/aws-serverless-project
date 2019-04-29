def lambda_handler(event, context):
    print(event)
    response = {
        "statusCode": 200,
        "body": "Hello I hope this works!!"
    }
    return response
