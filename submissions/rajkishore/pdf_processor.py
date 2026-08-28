from pypdf import PdfReader

def extract_text(uploaded_file):

    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n\n"

    return text

def chunk_text(text, chunk_size, overlap):

    chunks = []
    start = 0

    while start < len(text):
        chunk = text[start : start + chunk_size]
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks