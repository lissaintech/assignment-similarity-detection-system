from app.services.similarity_service import SimilarityService

service = SimilarityService()

service.add_assignment("storage/uploads/sample.png", "sample.png")

results = service.check_similarity("storage/uploads/sample.png")

print(results)
