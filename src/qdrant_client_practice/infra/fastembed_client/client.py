from fastembed import TextEmbedding
from qdrant_client_practice.config.config import condif

_TEXT_EMBED: TextEmbedding = None

def get_embed_model() -> TextEmbedding:
    if not _TEXT_EMBED:
        _TEXT_EMBED = TextEmbedding(condif.embed_client_config.model_name)
    return _TEXT_EMBED