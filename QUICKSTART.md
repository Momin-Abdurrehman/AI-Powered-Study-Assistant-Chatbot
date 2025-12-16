# Quick Start Guide

This guide will help you get up and running with the AI-Powered Study Assistant in minutes.

## Prerequisites

- Python 3.8 or higher
- An OpenAI API key (get one at https://platform.openai.com/api-keys)
- PDF files of your course notes or textbooks

## Installation Steps

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- LangChain for RAG orchestration
- sentence-transformers for embeddings
- ChromaDB for vector storage
- OpenAI Python SDK
- PyPDF for PDF processing

### 2. Set Up Your API Key

Copy the example environment file:
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### 3. Verify Installation

Run the verification script:
```bash
python verify.py
```

You should see:
```
✓ All verification checks passed!
```

## Using the Application

### Start the Chatbot

```bash
python main.py
```

### Upload Your First PDF

At the prompt, type:
```
upload /path/to/your/course_notes.pdf
```

The application will:
1. Load and parse the PDF
2. Split it into chunks
3. Create embeddings
4. Store in the vector database

### Ask Questions

After uploading, ask questions:
```
ask What is the definition of machine learning?
```

You'll receive:
- A comprehensive answer based on your documents
- Citations with page numbers
- Relevant excerpts from the source material

### Other Commands

- `list` - See all uploaded documents
- `clear` - Remove all documents (start fresh)
- `help` - Show available commands
- `quit` - Exit the application

## Example Session

```
> upload machine_learning_notes.pdf
Processing PDF: machine_learning_notes.pdf
Created 45 text chunks from the document
Added document to knowledge base

> ask What are the three types of machine learning?

Searching for relevant information...
================================================================================
ANSWER:
The three types of machine learning are:
1. Supervised Learning - Learning from labeled data
2. Unsupervised Learning - Finding patterns in unlabeled data
3. Reinforcement Learning - Learning through trial and error
(Based on Page 5 of machine_learning_notes.pdf)
================================================================================
CITATIONS:

[1] Page 5 (Relevance: 0.92)
    Source: machine_learning_notes.pdf
    Excerpt: The three main types of machine learning are supervised learning,
    unsupervised learning, and reinforcement learning...

[2] Page 6 (Relevance: 0.85)
    Source: machine_learning_notes.pdf
    Excerpt: In supervised learning, we train models on labeled examples...
================================================================================

> quit
Thank you for using the Study Assistant. Goodbye!
```

## Tips for Best Results

1. **Upload Quality PDFs**: Text-based PDFs work best (not scanned images)
2. **Ask Specific Questions**: More specific questions get better answers
3. **Upload Related Documents**: Upload all relevant course materials together
4. **Review Citations**: Check the citations to verify the answer context

## Troubleshooting

### "OPENAI_API_KEY not found"
- Make sure you created a `.env` file
- Check that your API key is valid and properly formatted

### "PDF file not found"
- Use absolute paths or ensure you're in the correct directory
- Check that the file exists and is a valid PDF

### Slow First Query
- The first query downloads the embedding model (~80MB)
- Subsequent queries are much faster

### Out of Memory
- Try processing smaller PDFs
- Reduce chunk_size in `DocumentProcessor` initialization
- Close and restart the application to free memory

## Next Steps

- Upload multiple course PDFs
- Experiment with different question types
- Use for exam preparation and studying
- Integrate into your own Python projects (see `example_usage.py`)

## Getting Help

- Check the main README.md for detailed documentation
- Review `example_usage.py` for programmatic usage
- Open an issue on GitHub for bug reports or feature requests

Happy studying! 📚🎓
