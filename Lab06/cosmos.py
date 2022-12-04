import json
from azure.cosmos import CosmosClient, PartitionKey

COSMOS_URI = "https://lcretu-cosmos-database.documents.azure.com:443/"
COSMOS_KEY = "MF6jQMWvKioz9pfgYvNOJFqjzxn6Xx2iny9uTWrzJaaYYCBo2oejNwn56nwqomkH6ZdcUdYomxBEACDboXpZ1g=="

client = CosmosClient(url=COSMOS_URI, credential=COSMOS_KEY)
database = client.create_database_if_not_exists(id="books-database")
partitionKeyPath = PartitionKey(path="/id")

container = database.create_container_if_not_exists(
	id="books",
	partition_key=partitionKeyPath
)

# Get all books
print('Query all books:')
query = "SELECT * FROM books"
items = container.query_items(
	query=query,
	enable_cross_partition_query=True
)

for item in items:
	print(json.dumps(item, indent=True))

# Add new book
print('Add new book:')
from uuid import uuid4
book_id = str(uuid4())
new_book = {
	"id": book_id,
	"name": "Iustin Cuceritorul",
	"author": "Iustin Tugui Ion",
	"publishingHouse": "Pitesti Hoping Center",
	"pages": 345
}
container.create_item(new_book)

# Read book
print('Read one book:')
book = container.read_item(
	item="aa2d021d-81e7-4e58-904a-159e1b6f5867",
	partition_key="aa2d021d-81e7-4e58-904a-159e1b6f5867"
)
print(json.dumps(book))

# Read books
print('Read 10 books:')
books = list(container.read_all_items(max_item_count=10))
for book in books:
	print(json.dumps(book))

# Replace book
print('Replace book:')
book = container.read_item(
	item="aa2d021d-81e7-4e58-904a-159e1b6f5867",
        partition_key="aa2d021d-81e7-4e58-904a-159e1b6f5867"
)
book['author'] = 'Alinut'
response = container.replace_item(item=book, body=book)
print(response)

# Upsert book
print('Upsert book:')
book = container.read_item(
        item="aa2d021d-81e7-4e58-904a-159e1b6f5867",
        partition_key="aa2d021d-81e7-4e58-904a-159e1b6f5867"
)
book['author'] = 'Alinut'
response = container.upsert_item(body=book)
print(response)

# Delete book
print('Replace book:')
response = container.delete_item(
        item="aa2d021d-81e7-4e58-904a-159e1b6f5867",
        partition_key="aa2d021d-81e7-4e58-904a-159e1b6f5867"
)
print(response)
