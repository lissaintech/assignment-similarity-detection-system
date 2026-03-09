from app.services.ocr_service import OCRService
from app.services.embedding_service import EmbeddingService
from app.db.faiss_db import FAISSDatabase
from app.services.chunking_service import ChunkingService


class SimilarityService:

    def __init__(self):
        self.ocr = OCRService()
        self.embedder = EmbeddingService()
        self.db = FAISSDatabase()
        self.chunker = ChunkingService()

    def add_assignment(self, file_path: str, file_name: str):

        text = self.ocr.extract_text(file_path)

        paragraphs = self.chunker.split_into_paragraphs(text)

        for i, paragraph in enumerate(paragraphs):

            embedding = self.embedder.generate_text_embedding(paragraph)

            paragraph_id = f"{file_name}_p{i}"

            self.db.add_embedding(embedding, paragraph_id)

    def check_similarity(self, file_path: str):

        text = self.ocr.extract_text(file_path)

        paragraphs = self.chunker.split_into_paragraphs(text)

        all_results = []

        for paragraph in paragraphs:

            embedding = self.embedder.generate_text_embedding(paragraph)

            results = self.db.search(embedding)

            all_results.extend(results)

        formatted_results = []
        seen = set()

        for result in all_results:

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