
import os
import json
import boto3
from dotenv import load_dotenv

load_dotenv()

client = boto3.client(
    "bedrock-runtime",
    region_name=os.getenv("aws_region"),
    aws_access_key_id=os.getenv("aws_access_key_id"),
    aws_secret_access_key=os.getenv("aws_secret_access_key"),
)


# # Test 1: Amazon Titan Embeddings
# embedding_response = client.invoke_model(
#     modelId=os.getenv("bedrock_embed_model"),
#     body=json.dumps({
#         "inputText": "Hello Amazon Bedrock"
#     }),
#     contentType="application/json",
#     accept="application/json"
# )

# embedding_data = json.loads(
#     embedding_response["body"].read()
# )

# print("Embedding dimension:", embedding_data["embedding"])




# Test 2: Amazon Nova Lite
chat_response = client.converse(
    modelId=os.getenv("bedrock_chat_model"),
    messages=[
        {
            "role": "user",
            "content": [
                {"text": "Explain RAG in one sentence."}
            ]
        }
    ],
    inferenceConfig={"maxTokens": 200}
)

print(
    "Nova Response:",
    chat_response["output"]["message"]["content"][0]["text"]
)


# response = client.invoke_model(
#     modelId="amazon.titan-embed-text-v1",
#     body=json.dumps({
#         "inputText": "Hello Amazon Bedrock"
#     }),
#     contentType="application/json",
#     accept="application/json"
# )
# embedding_data = json.loads(response["body"].read())
# print(embedding_data)