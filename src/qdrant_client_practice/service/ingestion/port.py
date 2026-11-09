from typing import Protocol

class IngestionEmbeddings(Protocol):
    def ingest_document():
        ...