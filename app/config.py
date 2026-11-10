from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    aws_region: str
    aws_access_key_id: str
    aws_secret_access_key: str
    s3_bucket: str
    database_url: str
    bedrock_embed_model: str
    bedrock_chat_model: str
    embed_dim: int = 1536
    max_upload_bytes: int = 10485760
    pinecone_api_key: str
    pinecone_index_name: str = "atlas-proj-index"
    pinecone_cloud: str
    pinecone_region: str
    pinecone_ready_timeout: int = 180
    min_relevance: float = 0.25
    hitl_enabled: bool = False
    memory_turns: int = 6


@lru_cache
def setting() -> Settings:
    return Settings()

@lru_cache
def settings() -> Settings:
    return setting()