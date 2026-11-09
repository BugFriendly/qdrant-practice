from qdrant_client_practice.infra.fastembed_client.client import EmbedLib, get_embed_model
from qdrant_client_practice.service.document_chunking.markdown_chunk_v5_merge_chunk_document_id_parent_id import get_ingestion_pipeline
from qdrant_client_practice.service.ingestion.port import IngestionEmbeddings

from llama_index.core.schema import MetadataMode, BaseNode
from typing import List

class ResumeEmbedV1():
    def __init__(self):
        self.__embed_client:EmbedLib  = get_embed_model()
        self.__chunk_generator = get_ingestion_pipeline()

    def ingest_document(self):
        docs: List[BaseNode] = self.__chunk_generator.split_to_nodes()
        embed_doc_text:List[str] = [doc.get_content(metadata_mode=MetadataMode.EMBED) for doc in docs]
        vectors = self.__embed_client.create_embedings(embed_doc_text)
        for doc, v in zip(docs,vectors):
            doc.embedding = v
        return docs

def get_resume_embeddings() -> IngestionEmbeddings:
    return ResumeEmbedV1() 