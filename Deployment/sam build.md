sam build
=========

Use this command to build your Lambda source code and generate deployment artifacts that target Lambda's execution environment. By doing this, the functions that you build locally run in a similar environment in the AWS Cloud.

The `sam build` command iterates through the functions in your application, looks for a manifest file (such as `requirements.txt`) that contains the dependencies, and automatically creates deployment artifacts that you can deploy to Lambda using the `sam package` and `sam deploy` commands. You that can also use `sam build` in combination with other commands like `sam local invoke` to test your application locally.

To use this command, update your AWS SAM template to specify the path to your function's source code in the resource's Code or CodeUri property.

**Usage:**

`sam build [OPTIONS]`

**Examples:**

```
To build on your workstation, run this command in folder containing
SAM template. Built artifacts will be written to .aws-sam/build folder
$ sam build

To build inside a AWS Lambda like Docker container
$ sam build --use-container

To build & run your functions locally
$ sam build && sam local invoke

To build and package for deployment
$ sam build && sam package --s3-bucket <bucketname>
```

**Options:**

| Option                    | Description                                                                                                                                                                                                                                                    |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -b, --build-dir DIRECTORY | The path to a folder where the built artifacts are stored.                                                                                                                                                                                                     |
| -s, --base-dir DIRECTORY  | Resolves relative paths to the function's source code with respect to this folder. Use this if the AWS SAM template and your source code aren't in the same enclosing folder. By default, relative paths are resolved with respect to the template's location. |
| -u, --use-container       | If your functions depend on packages that have natively compiled dependencies, use this flag to build your function inside an AWS Lambda-like Docker container.                                                                                                |
| -m, --manifest PATH       | The path to a custom dependency manifest (ex: package.json) to use instead of the default one.                                                                                                                                                                 |
| -t, --template PATH       | The AWS SAM template file \[default: template.                                                                                                                                                                                                  |
| --parameter-overrides     | Optional. A string that contains AWS CloudFormation parameter overrides encoded as key-value pairs. Use the same format as the AWS CLI—for example, 'ParameterKey=KeyPairName, ParameterValue=MyKey ParameterKey=InstanceType,ParameterValue=t1.micro'.        |
| --skip-pull-image         | Specifies whether the command should skip pulling down the latest Docker image for Lambda runtime.                                                                                                                                                             |
| --docker-network TEXT     | The name or ID of an existing Docker network that Lambda Docker containers should connect to, along with the default bridge network. If this isn't specified, the Lambda containers only connect to the default bridge Docker network.                         |
| --profile TEXT            | The AWS credentials profile to use.                                                                                                                                                                                                                            |
| --region TEXT             | Sets the AWS Region of the service (for example, us-east-1).                                                                                                                                                                                                   |
| --debug                   | Turns on debug logging.                                                                                                                                                                                                                                        |
| --help                    | Shows this message and exits.                                                                                                                                                                                                                                  |

Additional Resources: [AWS SAM CLI Command Reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html)
