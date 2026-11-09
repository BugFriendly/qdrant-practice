from qdrant_client_practice.service.document_chunking.markdown_chunk_v5_merge_chunk_document_id_parent_id import get_ingestion_pipeline
from typing import List
from llama_index.core.schema import BaseNode
from qdrant_client_practice.service.ingestion.resume_embed_v1 import get_resume_embeddings

service = get_resume_embeddings()
nodes = service.ingest_document()
max_len_node_index = 0
# max_len_node = 600
# for i,node in enumerate(nodes):
#     cur_len = len(node.get_content())
#     if cur_len < max_len_node:
#         max_len_node = cur_len
#         max_len_node_index = i

print(f"node embedding: {nodes[max_len_node_index].embedding}\n metadata: {nodes[max_len_node_index].metadata}\n\n")
