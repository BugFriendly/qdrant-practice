from qdrant_client_practice.service.document_chunking.markdown_chunk_v5_merge_chunk_document_id_parent_id import get_ingestion_pipeline
from typing import List
from llama_index.core.schema import BaseNode

service = get_ingestion_pipeline()
nodes:List[BaseNode] = service.split_to_nodes()
max_len_node_index = 0
max_len_node = 600
for i,node in enumerate(nodes):
    cur_len = len(node.get_content())
    if cur_len < max_len_node:
        max_len_node = cur_len
        max_len_node_index = i

print(f"node: {nodes[max_len_node_index].__str__()}\n metadata: {nodes[max_len_node_index].metadata}\n\n")
print(f"node: {nodes[max_len_node_index-1].__str__()}\n metadata: {nodes[max_len_node_index-1].metadata}\n\n")
print(f"node: {nodes[max_len_node_index+1].__str__()}\n metadata: {nodes[max_len_node_index+1].metadata}\n\n")
