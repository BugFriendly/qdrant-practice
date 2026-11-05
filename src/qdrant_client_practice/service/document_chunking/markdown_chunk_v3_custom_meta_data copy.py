from llama_index.core import Document, SimpleDirectoryReader
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.core.schema import BaseNode
from pathlib import Path
from typing import List
from .port import DocumentChunker

class ResumeChunkerV3():
    def __init__(self):
        file_path = Path(__file__).resolve().parents[4] / 'docs'/ 'akshat_tripathi_resume_rag.md'
        reader = SimpleDirectoryReader(input_files=[file_path])
        self._md_parser = MarkdownNodeParser()
        self._resume_document: List[Document] = reader.load_data()

    def split_to_nodes(self) -> List[BaseNode]:
        resume_nodes: List[BaseNode] = self._md_parser.get_nodes_from_documents(documents=self._resume_document)
        result: List[BaseNode] = []
        for node in resume_nodes:
            # The chunk's own heading is its first line; header_path only holds the parents.
            first_line, _, body = node.get_content().partition("\n")
            if first_line.startswith("#"):
                title = first_line.lstrip("#").strip()
                # header_path already ends with the separator ("/" or "/h1/h2/").
                node.metadata["current_heading"] = title
                current_head_path:str = node.metadata.get("header_path", "/")
                current_head_path_list:List[str] = current_head_path.split("/")
                node.metadata["header_path"] = [s for s in current_head_path_list if s.strip() != ""]
                node.set_content(body.strip())
            if node.get_content():
                result.append(node)
        return result

def get_ingestion_pipeline() -> DocumentChunker:
    return ResumeChunkerV3()