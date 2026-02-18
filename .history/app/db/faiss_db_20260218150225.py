import faiss
import numpy as np
import os
import pickle


class FAISSDatabase:

    def __init__(self, dimension=384):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.metadata = []

        self.index_file = "storage/embeddings/faiss.index"
        self.metadata_file = "storage/embeddings/metadata.pkl"

        self._load()

    def add_embedding(self, embedding: np.ndarray, file_name: str):
        embedding = np.array([embedding]).astype("float32")

        self.index.add(embedding)

        self.metadata.append(file_name)

        self._save()

    def search(self, embedding: np.ndarray, top_k=5):
        embedding = np.array([embedding]).astype("float32")

        distances, indices = self.index.search(embedding, top_k)

        results = []

        for i, idx in enumerate(indices[0]):
            if idx < len(self.metadata):
                results.append({
                    "file_name": self.metadata[idx],
                    "distance": float(distances[0][i])
                })

        return results

    def _save(self):
        os.makedirs("storage/embeddings", exist_ok=True)

        faiss.write_index(self.index, self.index_file)

        with open(self.metadata_file, "wb") as f:
            pickle.dump(self.metadata, f)

    def _load(self):
        if os.path.exists(self.index_file):
            self.index = faiss.read_index(self.index_file)

        if os.path.exists(self.metadata_file):
            with open(self.metadata_file, "rb") as f:
                self.metadata = pickle.load(f)
