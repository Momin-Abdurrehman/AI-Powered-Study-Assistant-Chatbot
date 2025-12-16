"""
Vector store manager for storing and retrieving document embeddings.
"""
import os
from typing import List, Optional
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


class VectorStoreManager:
    """Manages vector storage and retrieval using ChromaDB and sentence-transformers."""
    
    def __init__(self, persist_directory: str = "./chroma_db", 
                 embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Initialize the vector store manager.
        
        Args:
            persist_directory: Directory to persist the vector database
            embedding_model: Name of the sentence-transformers model to use
        """
        self.persist_directory = persist_directory
        self.embedding_model_name = embedding_model
        
        # Initialize embeddings using sentence-transformers
        self.embeddings = HuggingFaceEmbeddings(
            model_name=embedding_model,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        
        # Initialize or load vector store
        self.vector_store: Optional[Chroma] = None
        if os.path.exists(persist_directory) and os.listdir(persist_directory):
            self._load_vector_store()
    
    def _load_vector_store(self):
        """Load existing vector store from disk."""
        try:
            self.vector_store = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings
            )
        except Exception as e:
            print(f"Warning: Could not load existing vector store: {e}")
            self.vector_store = None
    
    def add_documents(self, documents: List[Document]) -> None:
        """
        Add documents to the vector store.
        
        Args:
            documents: List of documents to add
        """
        if not documents:
            raise ValueError("No documents provided to add to vector store")
        
        if self.vector_store is None:
            # Create new vector store
            self.vector_store = Chroma.from_documents(
                documents=documents,
                embedding=self.embeddings,
                persist_directory=self.persist_directory
            )
        else:
            # Add to existing vector store
            self.vector_store.add_documents(documents)
        
        # Persist changes
        self.vector_store.persist()
    
    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        """
        Search for similar documents.
        
        Args:
            query: Query string
            k: Number of documents to return
            
        Returns:
            List of similar documents
        """
        if self.vector_store is None:
            raise ValueError("Vector store is empty. Please add documents first.")
        
        results = self.vector_store.similarity_search(query, k=k)
        return results
    
    def similarity_search_with_score(self, query: str, k: int = 4) -> List[tuple]:
        """
        Search for similar documents with similarity scores.
        
        Args:
            query: Query string
            k: Number of documents to return
            
        Returns:
            List of tuples (document, score)
        """
        if self.vector_store is None:
            raise ValueError("Vector store is empty. Please add documents first.")
        
        results = self.vector_store.similarity_search_with_score(query, k=k)
        return results
    
    def clear(self) -> None:
        """Clear the vector store."""
        if os.path.exists(self.persist_directory):
            import shutil
            shutil.rmtree(self.persist_directory)
        self.vector_store = None
