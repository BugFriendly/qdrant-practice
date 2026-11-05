from typing import Protocol, List
from llama_index.core.schema import BaseNode
# from llama_index.core.schema import 

class DocumentChunker(Protocol):
    async def split_to_nodes(self) -> List[BaseNode]:
        ...