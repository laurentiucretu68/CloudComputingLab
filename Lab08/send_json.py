from azure.storage.queue import (
	QueueClient,
	BinaryBase64EncodePolicy,
	BinaryBase64DecodePolicy
)
import os, uuid
import json
import pickle

connect_str = "DefaultEndpointsProtocol=https;AccountName=booksstorageaccount;AccountKey=hq2bIr5CDAgkglGsA1EeJElgjNgNgmmEKar7EOXqZO/AFpMyRSmZYsUByOtTaa5L3jRP76m+rqkU+ASt1TmCAQ==;EndpointSuffix=core.windows.net"
queue_name = "books-queue"
queue_client = QueueClient.from_connection_string(
	connect_str,
	queue_name,
	message_encode_policy = BinaryBase64EncodePolicy(),
	message_decode_policy = BinaryBase64DecodePolicy()
)

try:
	queue_client.create_queue()
except:
	pass

message = {
	"1": {
		"title": "Harry Potter 1",
		"author": "JK Rowling",
		"pages": 143,
	},
	"2": {
		"title": "1984",
		"author": "George Orwell",
		"pages": 326,
	},
}

print("Adding message: " + str(message))
print()
encoded_message = pickle.dumps(message)

# Trimitem mesajul
queue_client.send_message(encoded_message)
# Receptionam mesajul
messages = queue_client.receive_messages()

for message in messages:
	print("Dequeueing message: " + str(message.content))
	decoded_message = pickle.loads(message.content)
	print("Decoded message: " + str(decoded_message))
	queue_client.delete_message(message.id, message.pop_receipt)

