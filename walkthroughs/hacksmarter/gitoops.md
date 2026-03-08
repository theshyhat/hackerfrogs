# URL
https://www.hacksmarter.org/courses/d6c75815-8e7b-4d90-9ebf-c619176ae2d9/take/gitoops
# Concept
* gitea hacking
* AWS S3 bucket enumeration
* 
# Method of solve
## Starting Scans
* there are ports, `22` (SSH), `80` (HTTP), `443` (HTTPS), and `2222` (SSH) open
* when we inspect either webpage, it redirects us to the HTTPS version of the page
* the app we're dealing with is Gitea
* with a bit of poking around, we see that there's a `gitCorp/public` repo, as well as a user on the system `alexis`
* in that repo, in the `settings.tf` file, there is reference to an AWS S3 bucket
* we use the following command to enumerate it:
```
aws s3 ls s3://gitoops-4ulyqvxd8nn6hlsc/ --no-sign-request
```
* this lets us know there's a `gitcorp` directory we can also look at
```
aws s3 ls s3://gitoops-4ulyqvxd8nn6hlsc/gitcorp/ --no-sign-request
```
* and this points to a file named `terraform.tfstate`. We can download it:
```
aws s3 cp s3://gitoops-4ulyqvxd8nn6hlsc/gitcorp/terraform.tfstate . --no-sign-requestaws
```
* among the contents of this file are several SSH private keys
* we copy their contents to create proper SSH private keys
* in reality, all 3 of the keys are valid with the `alexis` account on port `22`
```
echo -e '<KEY CONTENTS>' > private.key
```



