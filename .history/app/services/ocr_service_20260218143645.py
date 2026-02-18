import os
import fitz
import cv2
import numpy as np
from paddleocr import PaddleOCR


class OCRService:

    def __init__(self):
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en', , show_log)

    def extract_text_from_image(self, image_path: str) -> str:
        result = self.ocr.ocr(image_path)

        extracted_text = []

        for line in result:
            for word_info in line:
                text = word_info[1][0]
                extracted_text.append(text)

        return " ".join(extracted_text)

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        document = fitz.open(pdf_path)

        full_text = []

        for page_number in range(len(document)):
            page = document.load_page(page_number)

            pix = page.get_pixmap()

            image = np.frombuffer(pix.samples, dtype=np.uint8)

            image = image.reshape(pix.height, pix.width, pix.n)

            temp_image_path = f"temp_page_{page_number}.png"

            cv2.imwrite(temp_image_path, image)

            page_text = self.extract_text_from_image(temp_image_path)

            full_text.append(page_text)

            os.remove(temp_image_path)

        return " ".join(full_text)

    def extract_text(self, file_path: str) -> str:
        if file_path.lower().endswith(".pdf"):
            return self.extract_text_from_pdf(file_path)

        return self.extract_text_from_image(file_path)
