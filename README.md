# AWS Serverless Project

# Installation

Installing the AWS SAM CLI on Linux

## Install the AWS SAM CLI Using Linuxbrew

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

## Install the AWS CLI Using pip

Prerequisites

  - Python 2 version 2.6.5+ or Python 3 version 3.3+
  - Windows, Linux, macOS, or Unix

If you already have pip and a supported version of Python, you can install the AWS CLI by using the following command. If you have Python version 3+ installed, we recommend that you use the pip3 command.

  `$ pip3 install awscli --upgrade --user`
