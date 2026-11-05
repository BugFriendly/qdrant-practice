from llama_index.core import Document, SimpleDirectoryReader
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.core.schema import BaseNode
from pathlib import Path
from typing import List
from .port import DocumentChunker

class ResumeChunkerV1():
    def __init__(self):
        file_path = Path(__file__).resolve().parents[4] / 'docs'/ 'akshat_tripathi_resume_rag.md'
        reader = SimpleDirectoryReader(input_files=[file_path])
        self._md_parser = MarkdownNodeParser()
        self._resume_document: List[Document] = reader.load_data()

    def split_to_nodes(self) -> List[BaseNode]:
        resume_nodes: List[BaseNode] = self._md_parser.get_nodes_from_documents(documents=self._resume_document)
        return resume_nodes

def get_ingestion_pipeline() -> DocumentChunker:
    return ResumeChunkerV1()