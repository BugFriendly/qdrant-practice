from qdrant_client.models import FieldCondition, Filter, MatchValue, PointStruct, ScoredPoint

from qdrant_client_practice.infra.qdrant_client.client import QdrantVectorClient

class ResumeChunkRepository():
    def __init__(self, client: QdrantVectorClient, collection: str, vector_size: int):
        self._client = client
        self._collection = collection
        self._vector_size = vector_size

    async def ensure_collection(self) -> bool:
        """Create the collection if missing. Returns True if it was created."""
        if not await self._client.collection_exists(self._collection):
            await self._client.create_collection(self._collection, self._vector_size)
            return True

        # An existing collection with another vector size would reject every upsert and search.
        size = await self._client.get_vector_size(self._collection)
        if size is not None and size != self._vector_size:
            raise ValueError(
                f"Collection '{self._collection}' has vector size {size}, "
                f"expected {self._vector_size}"
            )
        return False

    async def search(
        self,
        vector: list[float],
        limit: int = 5,
        section: str | None = None,
    ) -> list[ScoredPoint]:
        query_filter = None
        if section is not None:
            query_filter = Filter(must=[FieldCondition(key="section", match=MatchValue(value=section))])
        return await self._client.query(self._collection, vector, limit=limit, query_filter=query_filter)

    async def upsert(self, points: list[PointStruct]) -> None:
        """Insert new points, or overwrite the ones whose id already exists."""
        await self._client.upsert(self._collection, points)
