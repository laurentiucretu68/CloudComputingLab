from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connection_str = "DefaultEndpointsProtocol=https;AccountName=booksstorageaccount;AccountKey=hq2bIr5CDAgkglGsA1EeJElgjNgNgmmEKar7EOXqZO/AFpMyRSmZYsUByOtTaa5L3jRP76m+rqkU+ASt1TmCAQ==;EndpointSuffix=core.windows.net"
container_name = "books"
file_name = "Screenshot from 2022-11-22 00-53-39.png"

blob_service_client = BlobServiceClient.from_connection_string(connection_str)
blob_client = blob_service_client.get_blob_client(
	container=container_name,
	blob=file_name
)

# Upload image
with open(file=file_name, mode="rb") as data:
	blob_client.upload_blob(data, content_type="image/png")

print(blob_client.url)
