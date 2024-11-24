# Document Summarization Web Application

This project is a web-based application built using **Flask** that allows users to upload PDF or DOCX files, extract their text content, and generate a summary using a state-of-the-art pre-trained AI model. The model, **BART** (Bidirectional and Auto-Regressive Transformers), is fine-tuned for text summarization tasks and is part of the **transformers** library by Hugging Face. The application aims to help users quickly condense long documents into digestible summaries and key points.

## Features

- **File Upload**: Users can upload PDF or DOCX documents directly through the web interface.
- **Text Summarization**: The app uses a **pre-trained BART model** for generating human-readable summaries of the document’s content.
- **Key Points Extraction**: After summarizing the document, the summary is split into individual key points, making it easier to grasp the most important information.
- **Support for PDF and DOCX Formats**: The app can process both PDF and DOCX files, extracting and summarizing text content from these formats.

## AI Model Overview: BART for Text Summarization

The model used for text summarization in this project is **BART** (Bidirectional and Auto-Regressive Transformers). BART is a sequence-to-sequence model developed by Facebook AI and is designed specifically for NLP tasks like text generation, translation, and summarization.

### Why BART?
BART combines the strengths of two architectures:
- **Bidirectional**: It uses an encoder that processes the entire input sequence at once, making it capable of understanding the context of the entire document.
- **Auto-Regressive**: The decoder generates text step-by-step, which helps in producing coherent and high-quality summaries.

### Model Fine-Tuning for Summarization
The specific BART model used here is the **facebook/bart-large-cnn** model, which has been fine-tuned on a large corpus of data for the task of **abstractive summarization**. Abstractive summarization means that the model generates a summary by understanding the content and then rephrasing it, as opposed to extractive summarization, which involves selecting parts of the original text.

This model is capable of summarizing long documents (such as reports or articles) into short summaries, while maintaining key information and readability.

## Technologies Used

- **Flask**: A lightweight web framework used to build the user interface and handle server-side operations.
- **PyPDF2**: A Python library used to extract text content from PDF files.
- **python-docx**: A library for extracting text from DOCX (Microsoft Word) documents.
- **transformers**: Hugging Face's library that provides access to pre-trained models like BART for tasks such as summarization, translation, and text generation.
- **Hugging Face Model**: **facebook/bart-large-cnn**, a large-scale pre-trained BART model fine-tuned for text summarization.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/document-summarization.git
   cd document-summarization
