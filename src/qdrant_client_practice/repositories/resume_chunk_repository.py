from qdrant_client.models import FieldCondition, Filter, MatchValue, PointStruct, ScoredPoint

from qdrant_client_practice.infra.qdrant_client.client import get_qdrant_client
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client_practice.config.config import condif

class ResumeChunkRepositoryV1():
    def __init__(self, collection: str, vector_size: int):
        self._client = get_qdrant_client()
        self._collection = condif.qdrant_client_config.resume_connection_v1_vector_size
        self._vector_size = condif.embed_client_config.vector_size
    
