import faiss
import numpy as np
import os


def create_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(
        np.array(embeddings).astype("float32")
    )

    return index


def save_faiss_index(index):

    faiss.write_index(
        index,
        "data/vector_store/index.faiss"
    )


def load_faiss_index():

    return faiss.read_index(
        "data/vector_store/index.faiss"
    )

def add_embeddings_to_index(
    embeddings
):

    embeddings = (
        np.array(embeddings)
        .astype("float32")
    )

    index_path = (
        "data/vector_store/index.faiss"
    )

    dimension = embeddings.shape[1]

    if os.path.exists(index_path):

        index = faiss.read_index(
            index_path
        )

    else:

        index = faiss.IndexFlatL2(
            dimension
        )

    index.add(embeddings)

    faiss.write_index(
        index,
        index_path
    )

    return index
