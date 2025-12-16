# AI-Powered Study Assistant Chatbot

An intelligent study assistant that helps you learn from your course materials. Upload PDFs of your notes, textbooks, or course materials, and ask questions to get accurate answers with citations!

## Features

✨ **Upload Course PDFs/Notes**: Easily upload and process PDF documents containing your study materials

🔍 **RAG (Retrieval-Augmented Generation)**: Uses advanced RAG pipeline to retrieve relevant information before generating answers

🎯 **Accurate Answers with Citations**: Get answers backed by citations showing exact page numbers and source excerpts

🤖 **Powered by AI**: Leverages LangChain for RAG orchestration and OpenAI's GPT models for natural language understanding

📚 **Multiple Document Support**: Upload multiple PDFs and query across all your study materials

## Technology Stack

- **LangChain**: RAG pipeline orchestration and document processing
- **sentence-transformers**: High-quality embeddings for semantic search (all-MiniLM-L6-v2)
- **ChromaDB**: Vector database for efficient similarity search
- **OpenAI GPT**: Language model for generating comprehensive answers
- **PyPDF**: PDF document loading and parsing

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/Momin-Abdurrehman/AI-Powered-Study-Assistant-Chatbot.git
cd AI-Powered-Study-Assistant-Chatbot
```

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Set up your OpenAI API key**:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Usage

### Starting the Application

Run the chatbot:
```bash
python main.py
```

### Available Commands

- `upload <path>` - Upload a PDF file to the knowledge base
- `ask <question>` - Ask a question about your uploaded materials
- `list` - List all uploaded documents
- `clear` - Clear all uploaded documents from the knowledge base
- `help` - Show available commands
- `quit` - Exit the application

### Example Session

```
> upload course_notes.pdf
Processing PDF: course_notes.pdf
Created 45 text chunks from the document
Added document to knowledge base

> ask What is machine learning?
Searching for relevant information...
================================================================================
ANSWER:
Machine learning is a subset of artificial intelligence that enables computers 
to learn from data without being explicitly programmed. According to the course 
notes (Page 3), it involves algorithms that can identify patterns in data and 
make predictions or decisions based on those patterns.
================================================================================
CITATIONS:

[1] Page 3 (Relevance: 0.85)
    Source: course_notes.pdf
    Excerpt: Machine learning is a field of study that gives computers the 
    ability to learn without being explicitly programmed...

[2] Page 5 (Relevance: 0.78)
    Source: course_notes.pdf
    Excerpt: There are three main types of machine learning: supervised 
    learning, unsupervised learning, and reinforcement learning...
================================================================================
```

## How It Works

1. **Document Processing**: PDFs are loaded and split into manageable chunks with overlap for context continuity

2. **Embedding Generation**: Text chunks are converted to vector embeddings using sentence-transformers (all-MiniLM-L6-v2)

3. **Vector Storage**: Embeddings are stored in ChromaDB for efficient similarity search

4. **Question Answering**:
   - Your question is embedded using the same model
   - Most relevant document chunks are retrieved via similarity search
   - Retrieved context + question are sent to OpenAI GPT
   - GPT generates an answer based on the provided context
   - Citations are extracted and formatted with page numbers

## Project Structure

```
AI-Powered-Study-Assistant-Chatbot/
├── main.py                 # Main application entry point
├── document_processor.py   # PDF loading and text chunking
├── vector_store.py        # Vector database management
├── qa_system.py           # Question-answering with citations
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Configuration

You can customize the following parameters by modifying the initialization in the respective files:

- **Chunk size**: Default 1000 characters (in `DocumentProcessor`)
- **Chunk overlap**: Default 200 characters (in `DocumentProcessor`)
- **Embedding model**: Default "sentence-transformers/all-MiniLM-L6-v2" (in `VectorStoreManager`)
- **Number of retrieved documents**: Default 4 (in `QASystem.ask_question`)
- **OpenAI model**: Default "gpt-3.5-turbo" (in `QASystem` or via environment variable)

## Requirements

- Python 3.8+
- OpenAI API key (for answer generation)
- ~500MB disk space for sentence-transformers model (downloaded on first run)

## Troubleshooting

**Issue**: "OPENAI_API_KEY not found!"
- **Solution**: Make sure you've created a `.env` file with your OpenAI API key

**Issue**: PDF processing fails
- **Solution**: Ensure the PDF is not corrupted and is a valid text-based PDF (not scanned images)

**Issue**: Slow first query
- **Solution**: The first query downloads the sentence-transformers model (~80MB), subsequent queries are faster

## Future Enhancements

- [ ] Support for more document formats (DOCX, TXT, etc.)
- [ ] Web interface using Streamlit or Gradio
- [ ] Support for other LLM providers (Anthropic, local models)
- [ ] Conversation history and follow-up questions
- [ ] Multi-language support
- [ ] Export Q&A sessions to study notes

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built with [LangChain](https://github.com/langchain-ai/langchain)
- Embeddings by [sentence-transformers](https://github.com/UKPLab/sentence-transformers)
- Vector database by [ChromaDB](https://github.com/chroma-core/chroma)