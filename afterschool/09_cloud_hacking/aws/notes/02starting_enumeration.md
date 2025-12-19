# AWS Security Testing - Initial Enumeration Steps
## Get user info
```
aws sts get-caller-identity --profile ctf
```
You may see something like this in the output:
```
{
    "UserId": "AIDA2HVQ5NJFVNUNILUL5",
    "Account": "703671921227",
    "Arn": "arn:aws:iam::703671921227:user/cg-sns-user-cgidqxdszo37l9"
}
```
* this output would let us know our user name is `cg-sns-user-cgidqxdszo37l9`
* we will need our user name for certain CLI actions
## Enumerating S3 Buckets
* `s3` buckets are file repositories in AWS
* we can use this command to list them:
```
aws s3api list-buckets
```
* alternatively:
```
aws s3 ls
```
## Enumerating SNS
* `sns` is Simple Notification Service, which is a publish/subscribe messaging service used to send messages from one producer to many consumers at once
* we can use these commands:
* to get topics
```
aws sns list-topics
```
* to get our user's subscriptions
```
aws sns list-subscriptions
```
## Enumerating API Gateways
* `API Gateways` are managed services for creating, publishing, and securing APIs (REST, HTTP, and WebSocket) that act as a front door to backend services
* to list the API gateways, use this command:
```
aws apigateway get-rest-apis
```
## Enumerating IAM
* `IAM` is Identity and Access Management, and it is the authorization system of AWS
* it controls who can do what, on which AWS resources, and under what conditions
* we can list our users with this command:
```
aws iam list-users
```
* we can list out roles with this command:
```
aws iam list-roles
```
* this command lets you list out which groups exist on the system
### Group Enumeration
```
aws iam list-groups
```
* this command lets you list out the members of a specific group
```
aws iam get-group --group-name <group_name>
```
* this command will get the policies attached to a group
```
aws iam list-attached-group-policies --group-name <group_name>
```
### User Permissions
* this command lets you know what permissions you have (general policies)
```
aws iam list-attached-user-policies --user-name <your_username>
```
* this command lets you know what specific permissions you have (user-specific)
```
aws iam get-user-policy --user-name <your_username> --policy-name <policy_name>
```
