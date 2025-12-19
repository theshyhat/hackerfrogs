# Pre Setup - Installing AWS-Cli
* the following commands are for Debian Linux (Kali)
```
sudo apt update
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
* verify the info with the following:
```
aws --version
```
# Setup - Configuring Your Account
Use this command to configure the account
```
aws configure
```
* You will be prompted for the following:
  * `AWS Access Key ID`: this usually starts with the string `AKIA`
  * `AWS Secret Access Key`: this may look like a base64-encoded string, roughly 40 characters long
  * `Default region name`: this may be indicated with your other credentials, but you can default to `us-east-1` if nothing else is provided to you
  * `Default output format`: this can be `None` (JSON) or alternatively, `Text` or `Table`
