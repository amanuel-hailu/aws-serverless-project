def lambda_handler(event, context):
    print(event)
    return {"response": "Thanks for calling Mike"}



# def lambda_handler(event, context):
#     response = {
#         "statusCode": 200,
#         "body": "Hello World!!"
#     }
#     return response
