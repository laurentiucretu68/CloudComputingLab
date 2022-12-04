from azure.storage.queue import (
	QueueClient,
	BinaryBase64EncodePolicy,
	BinaryBase64DecodePolicy
)
import os, uuid
from base64 import b64decode

connect_str = "DefaultEndpointsProtocol=https;AccountName=booksstorageaccount;AccountKey=hq2bIr5CDAgkglGsA1EeJElgjNgNgmmEKar7EOXqZO/AFpMyRSmZYsUByOtTaa5L3jRP76m+rqkU+ASt1TmCAQ==;EndpointSuffix=core.windows.net"
queue_name = "books-queue"
queue_client = QueueClient.from_connection_string(connect_str, queue_name)
messages = queue_client.receive_messages()

for message in messages:
	print("Dequeueing message: " + message.content)
	queue_client.delete_message(message.id, message.pop_receipt)

