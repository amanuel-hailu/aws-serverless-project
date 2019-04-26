# Demo

### The below command allows you to run your serverless application locally for quick development and testing. When you run this command in a directory that contains your serverless functions and your AWS SAM template, it creates a local HTTP server that hosts all of your functions.

sam local start-api


### The below command invokes the function with an empty event.

sam local invoke --no-event HelloLambda


### Command to delete stack

aws cloudformation delete-stack --stack-name sam-demo-dev
