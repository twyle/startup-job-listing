from ..config import POSTS_INDEX_NAME, POSTS_INDEX_SETTINGS, POSTS_INDEX_MAPPINGS
from ..extensions import es_client

def recreate_index():
    """Rebuild the ES index."""
    es_client.options(ignore_status=404).indices.delete(index=POSTS_INDEX_NAME)

    es_client.indices.create(
        index=POSTS_INDEX_NAME,
        settings=POSTS_INDEX_SETTINGS,
        mappings=POSTS_INDEX_MAPPINGS,
    )