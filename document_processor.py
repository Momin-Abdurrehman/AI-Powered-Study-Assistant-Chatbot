"""
Document processor for loading and chunking PDF documents.
"""
import os
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class DocumentProcessor:
    """Handles PDF loading and text chunking."""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Initialize the document processor.
        
        Args:
            chunk_size: Size of text chunks
            chunk_overlap: Overlap between chunks for context continuity
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )
    
    def load_pdf(self, pdf_path: str) -> List[Document]:
        """
        Load a PDF file and return documents.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            List of Document objects
        """
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        return documents
    
    def chunk_documents(self, documents: List[Document]) -> List[Document]:
        """
        Split documents into smaller chunks.
        
        Args:
            documents: List of documents to chunk
            
        Returns:
            List of chunked documents
        """
        chunks = self.text_splitter.split_documents(documents)
        return chunks
    
    def process_pdf(self, pdf_path: str) -> List[Document]:
        """
        Load and chunk a PDF file in one step.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            List of chunked documents
        """
        documents = self.load_pdf(pdf_path)
        chunks = self.chunk_documents(documents)
        return chunks
