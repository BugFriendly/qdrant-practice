from fastembed import TextEmbedding
from fastembed.common.types import NumpyArray
from qdrant_client_practice.config.config import condif
from typing import List, Iterable, Protocol

class EmbedLibImp():
    def __init__(self):
        self.embed_client = TextEmbedding(condif.embed_client_config.model_name)
    def create_embedings(self,doc_list:List[str]) -> Iterable[NumpyArray]:
        vectors = self.embed_client.embed(doc_list)
        return vectors

class EmbedLib(Protocol):
    def create_embedings(self,doc_list:List[str]) -> Iterable[NumpyArray]:
        ...

_TEXT_EMBED: EmbedLib = None

def get_embed_model() -> EmbedLib:
    global _TEXT_EMBED
    if not _TEXT_EMBED:
        _TEXT_EMBED = EmbedLibImp()
    return _TEXT_EMBED