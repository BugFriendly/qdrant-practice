from qdrant_client import QdrantClient
from qdrant_client_practice.config.config import condif

_VECTOR_DB: QdrantClient | None  = None

def get_qdrant_client() -> QdrantClient:
    global _VECTOR_DB
    if _VECTOR_DB:
        _VECTOR_DB = QdrantClient(host=condif.qdrant_client_config.host,port=condif.qdrant_client_config.port)
    return _VECTOR_DB