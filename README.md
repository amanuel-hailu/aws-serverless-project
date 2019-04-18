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

*Note: AWS Access Key ID and AWS Secret Access Key are provided to you when creating a user in AWS*

```
AWS Access Key ID [None]:

AWS Secret Access Key [None]:

Default region name [None]:

Default output format [None]:
```

---


### Install the AWS SAM CLI Using Pip

Follow these steps to install the AWS SAM CLI by using Linuxbrew:

1. Verify that the Python version is 2.7 or 3.6.

* `python --version`

2. Verify that pip is installed.

* `pip --version`

3. Install aws-sam-cli.

* `pip install --user aws-sam-cli`


---

### Install Docker CE

##### Uninstall old versions

```
$ sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine

```

##### Install Docker CE

```
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
```
