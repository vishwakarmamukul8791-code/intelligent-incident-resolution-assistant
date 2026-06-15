import faiss
import numpy as np
import json
import os
def create_faiss_index(embeddings):

    dimension = len(embeddings[0])

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index

def search_similar_chunks(index, query_embedding, k=3):

    distances, indices = index.search(
        np.array([query_embedding]),
        k
    )

    return distances, indices




def save_index(index):

    faiss.write_index(
        index,
        "data/vector_store/faiss_index.bin"
    )

def load_index():

    if not os.path.exists(
        "data/vector_store/faiss_index.bin"
    ):
        return None

    return faiss.read_index(
        "data/vector_store/faiss_index.bin"
    )


def save_metadata(metadata):

    with open(
        "data/vector_store/metadata.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            metadata,
            file,
            indent=4
        )

def load_metadata():

    path = "data/vector_store/metadata.json"

    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []