import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

api_key = os.getenv("pinecone_api_key")
if not api_key:
    raise ValueError("pinecone_api_key is missing from .env")

pc = Pinecone(api_key=api_key)

pc.create_index(
    name="atlas-proj-index",
    dimension=1536,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1"),
)

print("Index created")