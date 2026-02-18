from app.db.faiss_db import FAISSDatabase
from app.services.embedding_service import EmbeddingService


db = FAISSDatabase()
embedder = EmbeddingService()

text1 = "This is assignment about machine learning"
text2 = "This document discusses neural networks"
text3 = "Cooking recipe for pasta"

emb1 = embedder.generate_text_embedding(text1)
emb2 = embedder.generate_text_embedding(text2)
emb3 = embedder.generate_text_embedding(text3)

db.add_embedding(emb1, "assignment1.txt")
db.add_embedding(emb2, "assignment2.txt")
db.add_embedding(emb3, "recipe.txt")

query = embedder.generate_text_embedding("machine learning homework")

results = db.search(query)

print(results)
