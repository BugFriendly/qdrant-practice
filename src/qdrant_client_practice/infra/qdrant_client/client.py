from types import TracebackType

from qdrant_client import AsyncQdrantClient
from qdrant_client.models import (
    Distance, ExtendedPointId, Filter, PointStruct, ScoredPoint, UpdateResult, VectorParams,
)

class QdrantVectorClient():
    def __init__(self, host: str, port: int, timeout: int | None = None):
        self._aclient = AsyncQdrantClient(host=host, port=port, timeout=timeout)

    async def __aenter__(self) -> "QdrantVectorClient":
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self.close()

    async def collection_exists(self, collection: str) -> bool:
        return await self._aclient.collection_exists(collection)

    async def create_collection(
        self,
        collection: str,
        vector_size: int,
        distance: Distance = Distance.COSINE,
    ) -> None:
        await self._aclient.create_collection(
            collection_name=collection,
            vectors_config=VectorParams(size=vector_size, distance=distance),
        )

    async def get_vector_size(self, collection: str) -> int | None:
        """Size of the default (unnamed) vector, or None if the collection has none."""
        vectors = (await self._aclient.get_collection(collection)).config.params.vectors
        # The default vector comes back either bare or as {"": VectorParams}.
        if isinstance(vectors, dict):
            vectors = vectors.get("")
        return vectors.size if isinstance(vectors, VectorParams) else None

    async def upsert(self, collection: str, points: list[PointStruct]) -> UpdateResult:
        return await self._aclient.upsert(collection_name=collection, points=points, wait=True)

    async def set_payload(
        self,
        collection: str,
        point_ids: list[ExtendedPointId],
        payload: dict,
    ) -> UpdateResult:
        return await self._aclient.set_payload(
            collection_name=collection, payload=payload, points=point_ids, wait=True,
        )

    async def query(
        self,
        collection: str,
        vector: list[float],
        limit: int = 5,
        query_filter: Filter | None = None,
        with_payload: bool | list[str] = True,
    ) -> list[ScoredPoint]:
        response = await self._aclient.query_points(
            collection_name=collection,
            query=vector,
            limit=limit,
            query_filter=query_filter,
            with_payload=with_payload,
        )
        return response.points

    async def delete(self, collection: str, point_ids: list[ExtendedPointId]) -> UpdateResult:
        return await self._aclient.delete(
            collection_name=collection, points_selector=point_ids, wait=True,
        )

    async def close(self) -> None:
        await self._aclient.close()
