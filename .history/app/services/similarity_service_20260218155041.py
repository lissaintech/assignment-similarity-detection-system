from app.services.ocr_service import OCRService
from app.services.embedding_service import EmbeddingService
from app.db.faiss_db import FAISSDatabase


class SimilarityService:

    def __init__(self):
        self.ocr = OCRService()
        self.embedder = EmbeddingService()
        self.db = FAISSDatabase()

    def add_assignment(self, file_path: str, file_name: str):
        text = self.ocr.extract_text(file_path)

        embedding = self.embedder.generate_text_embedding(text)

        self.db.add_embedding(embedding, file_name)

    def check_similarity(self, file_path: str):
        text = self.ocr.extract_text(file_path)

        embedding = self.embedder.generate_text_embedding(text)

        results = self.db.search(embedding)

        formatted_results = []
        seen = set()

        for result in results:

            file_name = result["file_name"]
            distance = result["distance"]

            if file_name in seen:
                continue

            seen.add(file_name)

            similarity = max(0, 100 - (distance * 50))

            formatted_results.append({
                "file_name": file_name,
                "similarity_percentage": round(similarity, 2)
            })

        return formatted_results
