from azure.communication.email import EmailClient, EmailContent, EmailAddress, EmailMessage, EmailRecipients

connection_string = "endpoint=https://email-communication-lcretu.communication.azure.com/;accesskey=P8b4r9JYFPJsGfEj4r0w74Kb6nP3rfyJ9wXFEK0d2pQODDMx9/Y/0qxzCvGr4p4xfXr3mI+MwVHwvOE1GFgprA=="
client = EmailClient.from_connection_string(connection_string)

content = EmailContent(
	subject= "Test subject",
	plain_text= "Body text",
	html= "<html><h1>This is the body </h1></html>"
)

address = EmailAddress(email="laurentiucretu13@gmail.com", display_name="Laurentiu Cretu")
message = EmailMessage(
	sender="DoNotReply@35796574-76a6-4a66-b0bb-d8ef77996262.azurecomm.net",
	content=content,
	recipients=EmailRecipients(to=[address])
)

response = client.send(message)
print(response)
