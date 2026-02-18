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

        embedding = self.embefrom app.services.ocr_service import OCRService
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

        embedding = self.embe
