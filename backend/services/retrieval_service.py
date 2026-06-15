from backend.services.embedding_service import generate_embeddings
from backend.services.faiss_service import load_faiss_index
from backend.services.vector_store import load_metadata


def search_similar_chunks(query):

    query_embedding = generate_embeddings(
        [query]
    )

    index = load_faiss_index()

    distances, indices = index.search(
        query_embedding,
        5
    )

    metadata = load_metadata()

    results = []

    for idx in indices[0]:

        if idx < len(metadata):

            results.append(
                metadata[idx]
            )

    return results


def get_context(results):

    context = ""

    for result in results:

        context += result["chunk"]
        context += "\n\n"

    return context