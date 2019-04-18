# AWS Serverless Project

## Installation

### Install the AWS CLI Using pip

Prerequisites

  - Python 2 version 2.6.5+ or Python 3 version 3.3+

If you already have pip and a supported version of Python, you can install the AWS CLI by using the following command.

`pip install awscli --upgrade --user`

Then Verify that the AWS CLI installed correctly by running:

`aws --version`

### Configure the AWS CLI

For general use, the aws configure command is the fastest way to set up your AWS CLI installation.

`AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json`


### Install the AWS SAM CLI Using Linuxbrew

Follow these steps to install the AWS SAM CLI by using Linuxbrew:

1. To install the Linuxbrew package manager, follow the instructions on the Linuxbrew webiste (http://linuxbrew.sh/).

2. Upgrade Linuxbrew, and update it to the latest version.

  `brew upgrade`
  `brew update`

3. Add a brew tap from GitHub (https://github.com/aws/homebrew-tap).

  `brew tap aws/tap`

4. Install aws-sam-cli from the brew tap.

  `brew install aws-sam-cli`

  Now sam is installed to the following location:

  `/home/linuxbrew/.linuxbrew/bin/sam`

  You should be able to invoke sam from the command line.

  `sam --version`

---



  `$ pip3 install awscli --upgrade --user`
