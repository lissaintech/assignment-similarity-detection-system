import re


class ChunkingService:

    def split_into_paragraphs(self, text: str):
        paragraphs = re.split(r'\n\s*\n', text)

        cleaned = []

        for p in paragraphs:
            p = p.strip()

            if len(p) > 30:
                cleaned.append(p)

        return cleaned