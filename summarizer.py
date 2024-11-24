from docx import Document
from PyPDF2 import PdfReader
from transformers import pipeline

# Load the summarization model on CPU (device=-1 for CPU)
summarizer_model = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    """Extract text from a DOCX file."""
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def summarize_document(file_path):
    """Summarize the document's text."""
    # Extract text from the document
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or Word document.")

    # Limit the text length for summarization to fit the model's input size
    max_input_length = 3024  # This is the token limit, not the character limit.
    text = text[:max_input_length] if len(text) > max_input_length else text

    # Generate the summary using the BART model
    summary = summarizer_model(text, max_length=1000, min_length=300, do_sample=False)
    
    return summary[0]['summary_text']
