from llama_index.core import Document, SimpleDirectoryReader
from llama_index.core.node_parser import MarkdownNodeParser, SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.schema import BaseNode
from qdrant_client_practice.config.config import condif
from .port import DocumentChunker
from qdrant_client_practice.static.docs_info import DOC_ID
from pathlib import Path
from typing import List

class ResumeChunkerV5():
    def __init__(self):
        file_path = Path(__file__).resolve().parents[4] / 'docs'/ 'akshat_tripathi_resume_rag.md'
        reader = SimpleDirectoryReader(input_files=[file_path])
        self._ingestion_pipeline = IngestionPipeline(transformations=[MarkdownNodeParser(),SentenceSplitter(chunk_size=condif.qdrant_client_config.chunk_size,chunk_overlap=condif.qdrant_client_config.chunk_loverlap)])
        self._resume_document: List[Document] = reader.load_data()

    def __deterministic_node_id(slef,node_index:int) -> str:
        return f"{DOC_ID.__str__()}-{node_index}"

    def split_to_nodes(self) -> List[BaseNode]:
        resume_nodes: List[BaseNode] = self._ingestion_pipeline.run(documents=self._resume_document)
        result: List[BaseNode] = []
        parent_map: map[str,str] = {}
        for i,node in enumerate(resume_nodes):
            node.id_ = self.__deterministic_node_id(i)
            # The chunk's own heading is its first line; header_path only holds the parents.
            first_line, _, body = node.get_content().partition("\n")
            if first_line.startswith("#"):
                title = first_line.lstrip("#").strip()
                # header_path already ends with the separator ("/" or "/h1/h2/").
                current_parent = node.metadata.get("header_path")
                parent_id = parent_map.get(current_parent)
                if current_parent and parent_id:
                    node.metadata["parent_id"] = parent_id
                new_title = node.metadata.get("header_path", "/") + "/" + title
                print(new_title)
                parent_map[new_title] = new_title
                node.metadata["header_path"] = new_title
                node.metadata["doc_id"] = DOC_ID.__str__()
                node.set_content(body.strip())
            if node.get_content():
                result.append(node)
        return result

def get_ingestion_pipeline() -> DocumentChunker:
    return ResumeChunkerV5()
