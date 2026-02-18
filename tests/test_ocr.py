from app.services.ocr_service import OCRService

ocr = OCRService()

file_path = "storage/uploads/sample.png"

text = ocr.extract_text(file_path)

print("\nExtracted Text:\n")
print(text)
