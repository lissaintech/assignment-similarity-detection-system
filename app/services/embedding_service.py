from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingService:

    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def generate_text_embedding(self, text: str) -> np.ndarray:
        embedding = self.model.encode(text)
        return embedding

    def generate_batch_embeddings(self, texts: list[str]) -> list[np.ndarray]:
        embeddings = self.model.encode(texts)
        return embeddings
