"""
Example script demonstrating programmatic usage of the Study Assistant.
This shows how to integrate the chatbot into other Python applications.
"""
import os
from dotenv import load_dotenv
from document_processor import DocumentProcessor
from vector_store import VectorStoreManager
from qa_system import QASystem


def example_usage():
    """Example of using the Study Assistant programmatically."""
    
    # Load environment variables
    load_dotenv()
    
    print("="*80)
    print("Study Assistant - Programmatic Usage Example")
    print("="*80)
    
    # Step 1: Initialize components
    print("\n1. Initializing components...")
    doc_processor = DocumentProcessor(chunk_size=1000, chunk_overlap=200)
    vector_store = VectorStoreManager(persist_directory="./example_chroma_db")
    
    # Step 2: Process a PDF (you would replace this with your actual PDF path)
    print("\n2. Processing documents...")
    print("   (In this example, you would upload actual PDF files)")
    print("   Example: chunks = doc_processor.process_pdf('my_textbook.pdf')")
    print("           vector_store.add_documents(chunks)")
    
    # Step 3: Initialize QA system
    print("\n3. Initializing QA system...")
    print("   Example: qa_system = QASystem(vector_store)")
    
    # Step 4: Ask questions
    print("\n4. Asking questions...")
    print("   Example: response = qa_system.ask_question('What is machine learning?')")
    print("           print(qa_system.format_response(response))")
    
    print("\n" + "="*80)
    print("Complete Workflow:")
    print("="*80)
    print("""
# Initialize
doc_processor = DocumentProcessor()
vector_store = VectorStoreManager()

# Upload and process PDF
chunks = doc_processor.process_pdf('course_notes.pdf')
vector_store.add_documents(chunks)

# Create QA system
qa_system = QASystem(vector_store)

# Ask questions
response = qa_system.ask_question('Explain photosynthesis')
formatted = qa_system.format_response(response)
print(formatted)

# The response includes:
# - answer: The generated answer
# - sources: List of source document paths
# - citations: Detailed citations with page numbers and excerpts
    """)
    print("="*80)
    
    # Cleanup example database
    if os.path.exists("./example_chroma_db"):
        import shutil
        shutil.rmtree("./example_chroma_db")
    
    print("\nFor a fully interactive experience, run: python main.py")


if __name__ == "__main__":
    example_usage()
