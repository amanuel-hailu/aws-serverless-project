# aws-serverless-project

# Installation

Installing the AWS SAM CLI on Linux

Install the AWS SAM CLI Using Linuxbrew
Follow these steps to install the AWS SAM CLI by using Linuxbrew:

To install the Linuxbrew package manager, follow the instructions on the Linuxbrew website.

Upgrade Linuxbrew, and update it to the latest version.

brew upgrade
brew update
Add a brew tap from GitHub.

brew tap aws/tap
Install aws-sam-cli from the brew tap.

brew install aws-sam-cli
Now sam is installed to the following location:

/home/linuxbrew/.linuxbrew/bin/sam
You should be able to invoke sam from the command line.

sam --version
