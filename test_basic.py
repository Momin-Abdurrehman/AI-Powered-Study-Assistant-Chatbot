"""
Simple test script to verify the core functionality.
This script tests the basic flow without requiring user interaction.
"""
import os
import sys
from dotenv import load_dotenv

# Test imports
try:
    from document_processor import DocumentProcessor
    from vector_store import VectorStoreManager
    from qa_system import QASystem
    print("✓ All modules imported successfully")
except ImportError as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)


def test_document_processor():
    """Test document processor initialization."""
    try:
        processor = DocumentProcessor(chunk_size=500, chunk_overlap=50)
        print("✓ DocumentProcessor initialized")
        return True
    except Exception as e:
        print(f"✗ DocumentProcessor error: {e}")
        return False


def test_vector_store():
    """Test vector store initialization."""
    try:
        # Use a test directory
        vector_store = VectorStoreManager(persist_directory="./test_chroma_db")
        print("✓ VectorStoreManager initialized")
        
        # Clean up
        if os.path.exists("./test_chroma_db"):
            import shutil
            shutil.rmtree("./test_chroma_db")
        
        return True
    except Exception as e:
        print(f"✗ VectorStoreManager error: {e}")
        return False


def test_environment():
    """Test environment setup."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key and api_key != "your_openai_api_key_here":
        print("✓ OPENAI_API_KEY is configured")
        return True
    else:
        print("⚠ OPENAI_API_KEY not configured (required for full functionality)")
        return False


def main():
    """Run all tests."""
    print("="*80)
    print("Running Study Assistant Tests")
    print("="*80)
    print()
    
    results = []
    
    print("Testing environment setup...")
    results.append(test_environment())
    print()
    
    print("Testing document processor...")
    results.append(test_document_processor())
    print()
    
    print("Testing vector store...")
    results.append(test_vector_store())
    print()
    
    print("="*80)
    if all(results[:2]):  # First two tests must pass
        print("✓ Core components are working correctly!")
        if not results[2]:
            print("\nNote: Set up your OpenAI API key in .env to use the full functionality")
    else:
        print("✗ Some tests failed. Please check the errors above.")
        sys.exit(1)
    print("="*80)


if __name__ == "__main__":
    main()
