"""
Question-Answering system with citations using RAG.
"""
import os
from typing import List, Dict, Any
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from vector_store import VectorStoreManager


class QASystem:
    """Question-Answering system with citation support."""
    
    def __init__(self, vector_store_manager: VectorStoreManager, 
                 model_name: str = "gpt-3.5-turbo", temperature: float = 0.0):
        """
        Initialize the QA system.
        
        Args:
            vector_store_manager: Vector store manager for document retrieval
            model_name: OpenAI model to use
            temperature: Temperature for response generation
        """
        self.vector_store_manager = vector_store_manager
        
        # Initialize OpenAI chat model
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            openai_api_key=api_key
        )
        
        # Define prompt template
        self.prompt_template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Always cite the source of your information by mentioning the page number when available.

Context:
{context}

Question: {question}

Answer with citations (mention page numbers):"""

        self.prompt = PromptTemplate(
            template=self.prompt_template,
            input_variables=["context", "question"]
        )
    
    def ask_question(self, question: str, k: int = 4) -> Dict[str, Any]:
        """
        Ask a question and get an answer with citations.
        
        Args:
            question: The question to ask
            k: Number of relevant documents to retrieve
            
        Returns:
            Dictionary with 'answer', 'sources', and 'citations'
        """
        # Retrieve relevant documents
        docs_with_scores = self.vector_store_manager.similarity_search_with_score(question, k=k)
        
        if not docs_with_scores:
            return {
                "answer": "I don't have any documents to answer this question.",
                "sources": [],
                "citations": []
            }
        
        # Prepare context from retrieved documents
        context_parts = []
        citations = []
        
        for i, (doc, score) in enumerate(docs_with_scores):
            page_num = doc.metadata.get('page', 'unknown')
            source = doc.metadata.get('source', 'unknown')
            
            context_parts.append(f"[Source {i+1} - Page {page_num}]:\n{doc.page_content}\n")
            citations.append({
                'source': source,
                'page': page_num,
                'score': float(score),
                'excerpt': doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content
            })
        
        context = "\n".join(context_parts)
        
        # Generate answer using LLM
        formatted_prompt = self.prompt.format(context=context, question=question)
        answer = self.llm.predict(formatted_prompt)
        
        return {
            "answer": answer,
            "sources": [c['source'] for c in citations],
            "citations": citations
        }
    
    def format_response(self, response: Dict[str, Any]) -> str:
        """
        Format the response for display.
        
        Args:
            response: Response dictionary from ask_question
            
        Returns:
            Formatted string
        """
        output = f"\n{'='*80}\n"
        output += f"ANSWER:\n{response['answer']}\n"
        output += f"\n{'='*80}\n"
        output += "CITATIONS:\n"
        
        for i, citation in enumerate(response['citations'], 1):
            output += f"\n[{i}] Page {citation['page']} (Relevance: {1-citation['score']:.2f})\n"
            output += f"    Source: {os.path.basename(citation['source'])}\n"
            output += f"    Excerpt: {citation['excerpt']}\n"
        
        output += f"{'='*80}\n"
        return output
