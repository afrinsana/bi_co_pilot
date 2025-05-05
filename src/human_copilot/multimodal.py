from PIL import Image
import pytesseract  # OCR for images
import PyPDF2

class MultiModalProcessor:
    def extract_text_from_image(self, image_path: str) -> str:
        """Extract text from an image using OCR."""
        return pytesseract.image_to_string(Image.open(image_path))
    
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract text from a PDF."""
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = "\n".join([page.extract_text() for page in reader.pages])
        return text

# Example usage:
# processor = MultiModalProcessor()
# print(processor.extract_text_from_image("notes.png"))
# print(processor.extract_text_from_pdf("doc.pdf"))