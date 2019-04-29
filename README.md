# AWS SAM Demo

This example implements a very simple Hello World API using AWS Lambda and AWS API Gateway

## Goal

The goal of this exercise is to learn how to write a very simple Lambda, test it locally and deploy it on AWS

### Step one (Installation)

Install the necessary software's needed for this demonstration [Installation](/Installation/README.md)  

### Step Two (Validate yaml file)

With aws-sam-local you can test if your template.yaml file is valid by typing

`sam validate -t [NameOfTemplate]`

### Step Three (Test locally)

With aws-sam-local installed and your shell in this project folder, run:

`sam local start-api`  

### Step Four (Deploy on AWS)

You can deploy on your AWS account with the following script ([deploy.sh](deploy.sh))

```
#!/bin/bash

# dev:   ./deploy.sh
# prod:  ./deploy.sh prod
STAGE=${1:-dev}
PROJECT=sam-demo$STAGE

# The bucket has to be unique
BUCKET=$PROJECT-testing-stack

# make a build directory to store artifacts
rm -rf build
mkdir build

# make the deployment bucket in case it doesn't exist
aws s3 mb s3://$BUCKET

# generate next stage yaml file
sam package                   \
    --template-file template.yaml            \
    --output-template-file build/output.yaml \
    --s3-bucket $BUCKET

# the actual deployment step
sam deploy                     \
    --template-file build/output.yaml         \
    --stack-name $PROJECT                     \
    --capabilities CAPABILITY_IAM             \
    --parameter-overrides Environment=$STAGE

```

#### Additional Commands:

##### Command to delete stack

The below command will delete all the resources that were created when deploying (resources that were defined in [template.yaml](template.yaml))

`aws cloudformation delete-stack --stack-name sam-demo-dev`
