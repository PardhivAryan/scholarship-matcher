from elasticsearch import Elasticsearch
from app.config import settings

es = Elasticsearch(settings.ES_HOST)

def search_scholarships(query: str):
    response = es.search(
        index=settings.ES_INDEX,
        body={
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["name", "provider", "description"],
                }
            }
        },
    )
    # return simplified docs
    hits = []
    for hit in response["hits"]["hits"]:
        src = hit["_source"]
        hits.append(
            {
                "id": hit.get("_id"),
                "name": src.get("name"),
                "provider": src.get("provider"),
                "description": src.get("description"),
                "score": hit.get("_score"),
            }
        )
    return hits
