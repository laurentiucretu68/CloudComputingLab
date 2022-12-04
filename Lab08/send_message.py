from azure.storage.queue import (
	QueueClient,
	BinaryBase64EncodePolicy,
	BinaryBase64DecodePolicy
)
import os, uuid
connect_str = "DefaultEndpointsProtocol=https;AccountName=booksstorageaccount;AccountKey=hq2bIr5CDAgkglGsA1EeJElgjNgNgmmEKar7EOXqZO/AFpMyRSmZYsUByOtTaa5L3jRP76m+rqkU+ASt1TmCAQ==;EndpointSuffix=core.windows.net"
queue_name = "books-queue"
queue_client = QueueClient.from_connection_string(connect_str, queue_name)
messages = [
	"test-1",
	"test-2",
	"test-3",
]

for message in messages:
	print("Adding message: " + message)
	queue_client.send_message(message)

