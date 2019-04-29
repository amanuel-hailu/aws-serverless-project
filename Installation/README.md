# Installation

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

1. First, let's update the package database:

```
sudo yum check-update
```

2. Now run this command. It will add the official Docker repository, download the latest version of Docker, and install it:

```
curl -fsSL https://get.docker.com/ | sh
```

3. Start Docker

```
sudo systemctl start docker
```
4. Verify that it's running:

```
sudo systemctl status docker
```

5. Executing Docker Command Without Sudo (Optional)

a. If you want to avoid typing sudo whenever you run the docker command, add your username to the docker group:

```
sudo usermod -aG docker $(whoami)
```

*Note: You will need to log out of the Droplet and back in as the same user to enable this change*

6. To check whether you can access and download images from Docker Hub, type:

```
docker run hello-world
```

*Note: This command downloads a test image and runs it in a container. When the container runs, it prints an informational message and exits*

7. Configure Docker to start on boot

You can configure docker to start on boot with the following command:

```
sudo systemctl enable docker
```

---

### Install the AWS CLI Using pip

Prerequisites

  - Python 2 version 2.6.5+ or Python 3 version 3.3+

If you already have pip and a supported version of Python, you can install the AWS CLI by using the following command.

`pip install awscli --upgrade --user`

Then Verify that the AWS CLI installed correctly by running:

`aws --version`

Additional Resources: [Installing pip and AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-linux.html)

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

### Install the AWS SAM CLI Using Using Linuxbrew

Follow these steps to install the AWS SAM CLI by using Linuxbrew:

1. To install the Linuxbrew package manager, follow the instructions on the [Linuxbrew website](https://docs.brew.sh/Homebrew-on-Linux).


2. Upgrade Linuxbrew, and update it to the latest version

```
brew upgrade
brew update
```

3. Add a brew tap from GitHub

`brew tap aws/tap`

4. Install aws-sam-cli from the brew tap.

`brew install aws-sam-cli`

Additional Resources: [Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

---
