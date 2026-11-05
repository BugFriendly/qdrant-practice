from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

ROOT_PROJECT = Path(__file__).resolve().parents[3]

ENV_FILE = ROOT_PROJECT / ".env"

class QdrantConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = ENV_FILE,
        env_file_encoding="utf-8",
        env_prefix="QDRANT_",
        extra="ignore"
    )

    host: str
    port: int
    resume_connection_v1: str
    resume_connection_v2: str = ""
    resume_highbrid_collection: str
    chunk_size: int
    chunk_loverlap: int
    resume_connection_v1_vector_size: int

class Fastembed(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = ENV_FILE,
        env_file_encoding="utf-8",
        env_prefix="FASTEMBED_",
        extra="ignore"
    )

    model_name: str
    vector_size: int

class PostgresClient(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = ENV_FILE,
        env_file_encoding="utf-8",
        env_prefix="PG_",
        extra="ignore"
    )

class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = ENV_FILE,
        env_file_encoding="utf-8",
        env_prefix="APP_",
        extra="ignore"
    )

    host: str
    port: int
    qdrant_client_config: QdrantConfig = QdrantConfig()
    embed_client_config: Fastembed = Fastembed()

condif = AppConfig()