# Secrets Manager Overview
This is a service which keeps track of secrets such as database credentials, OAuth tokens and API keys
# Enumerating Secrets
## List Secrets
```
aws secretsmanager list-secrets
```
## Get value of secrets
```
aws secretsmanager get-secret-value --secret-id <secret_id_value>
```
