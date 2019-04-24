sam local generate-event - AWS Serverless Application Model                       

[![Amazon Web Services](./sam local generate-event_files/aws_logo_105x39.png)](http://aws.amazon.com/)

[Sign In to the Console](https://console.aws.amazon.com/console/home)

Deutsch English Español Français Italiano 日本語 한국어 Português 中文 (简体) 中文 (繁體)English

[](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-application-model-updates.rss "View RSS Feed")[](http://www.amazon.com/dp/B07P7K9VZB "Open Kindle")[](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-application-model.pdf#sam-cli-command-reference-sam-local-generate-event "Open PDF")[](https://github.com/awsdocs/aws-sam-developer-guide/tree/master/doc_source/sam-cli-command-reference-sam-local-generate-event.md "Edit on GitHub")

AWS Serverless Application Model

Developer Guide

Entire Site AMIs from AWS Marketplace AMIs from All Sources Articles & Tutorials AWS Product Information Case Studies Customer Apps Documentation Documentation - This Product Documentation - This Guide Public Data Sets Release Notes Partners Sample Code & Libraries  

*   [What Is AWS SAM?](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
*   [Quick Start](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-quick-start.html)
*   [AWS SAM Template Concepts](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-basics.html)
   *   [Declaring Serverless Resources](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template.html)
   *   [Declaring AWS CloudFormation Resources](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/appendix-appendix-sam-templates-and-cf-templates.html)
   *   [Nested Applications](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.html)
   *   [Controlling Access to APIs](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-controlling-access-to-apis.html)
*   [Testing and Debugging Serverless Applications](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-test-and-debug.html)
   *   [Building Applications with Dependencies](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-build.html)
   *   [Invoking Functions Locally](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-invoke.html)
   *   [Running API Gateway Locally](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-start-api.html)
   *   [Working with Layers](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-layers.html)
   *   [Running Automated Tests](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-automated-tests.html)
   *   [Generating Sample Event Payloads](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-generate-event.html)
   *   [Working with Logs](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html)
   *   [Step-Through Debugging Lambda Functions Locally](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging.html)
       *   [Node.js](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging-nodejs.html)
       *   [Python](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging-python.html)
       *   [Golang](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging-golang.html)
   *   [Passing Additional Runtime Debug Arguments](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging-additional-arguments.html)
   *   [Validating AWS SAM Template Files](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-validate.html)
*   [Deploying Serverless Applications](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-deploying.html)
   *   [Gradual Code Deployment](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html)
*   [Publishing Serverless Applications](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.html)
   *   [Metadata Section Properties](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications-metadata-properties.html)
*   [Example Applications](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-example-applications.html)
   *   [Process DynamoDB Events](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-example-ddb.html)
   *   [Process Amazon S3 Events](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-example-s3.html)
*   [AWS SAM Reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-reference.html)
   *   [Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
       *   [Linux](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-linux.html)
       *   [Windows](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-windows.html)
       *   [macOS](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html)
       *   [Additional Installation Topics](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-additional.html)
           *   [Adjusting Your Path on Linux](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-linux-path.html)
           *   [Adjusting Your Path on Windows](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-windows-path.html)
           *   [Adjusting Your Path on macOS](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac-path.html)
   *   [AWS SAM CLI Command Reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html)
       *   [sam build](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-build.html)
       *   [sam deploy](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-deploy.html)
       *   [sam init](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-init.html)
       *   [sam local generate-event](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html)
       *   [sam local invoke](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-invoke.html)
       *   [sam local start-api](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-start-api.html)
       *   [sam local start-lambda](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-start-lambda.html)
       *   [sam logs](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-logs.html)
       *   [sam package](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-package.html)
       *   [sam publish](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-publish.html)
       *   [sam validate](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-validate.html)
*   [Document History](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/doc-history.html)

[AWS Documentation](https://docs.aws.amazon.com/index.html) » [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/index.html) » [Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/index.html) » [AWS SAM Reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-reference.html) » [AWS SAM CLI Command Reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html) » sam local generate-event

Currently we are only able to display this content in English.

sam local generate-event
========================

Generates sample payloads from different event sources, such as Amazon S3, Amazon API Gateway, and Amazon SNS. These payloads contain the information that the event sources send to your Lambda functions.

**Usage:**

`sam local generate-event [OPTIONS] COMMAND [ARGS]...`

**Examples:**

`Generate the event that S3 sends to your Lambda function when a new object is uploaded
$ sam local generate-event s3 [put/delete]

You can even customize the event by adding parameter flags. To find which flags apply to your command,
run:

$ sam local generate-event s3 [put/delete] --help

Then you can add in those flags that you wish to customize using

$ sam local generate-event s3 [put/delete] --bucket <bucket> --key <key>

After you generate a sample event, you can use it to test your Lambda function locally
$ sam local generate-event s3 [put/delete] --bucket <bucket> --key <key> | sam local invoke <function logical id>`

**Options:**

Option

Description

\--help

Shows this message and exits.

**Commands:**

*   alexa-skills-kit

*   alexa-smart-home

*   apigateway

*   batch

*   cloudformation

*   cloudfront

*   cloudwatch

*   codecommit

*   codepipeline

*   cognito

*   config

*   dynamodb

*   kinesis

*   lex

*   rekognition

*   s3

*   ses

*   sns

*   sqs

*   stepfunctions


![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the AWS Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](https://docs.aws.amazon.com/general/latest/gr/docconventions.html)

[« Previous](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-init.html) [Next »](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-invoke.html)

© 2019, Amazon Web Services, Inc. or its affiliates. All rights reserved.

We use cookies to provide and improve our services. By using our site, you consent to cookies. [Learn more](http://aws.amazon.com/legal/cookies)

[Terms of Use](http://aws.amazon.com/terms) | [Privacy](http://aws.amazon.com/privacy) | © 2019, Amazon Web Services, Inc. or its affiliates. All rights reserved.

Did this page help you?

[Yes](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/feedbackyes.html?topic_url=http://docs.aws.amazon.com/en_us/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html)[No](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/feedbackno.html?topic_url=http://docs.aws.amazon.com/en_us/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html)

[Feedback](https://docs.aws.amazon.com/forms/aws-doc-feedback?hidden_service_name=Serverless%20Application%20Model&topic_url=http://docs.aws.amazon.com/en_us/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html&hidden_guide_name=Developer%20Guide&hidden_api_version=&hidden_file_name=sam-cli-command-reference-sam-local-generate-event)

<!-- // Documentation Service Name s.prop66='AWS Serverless Application Model'; s.eVar66='D=c66'; // Documentation Guide Name s.prop65='Developer Guide'; s.eVar65='D=c65'; var s\_code=s.t();if(s\_code)document.write(s\_code)//--> <!-- if(navigator.appVersion.indexOf('MSIE')>=0)document.write(unescape('%3C')+'\\!-'+'-') //-->

![](https://amazonwebservices.d2.sc.omtrdc.net/b/ss/awsamazondev/1/H.25.2--NS/0)
