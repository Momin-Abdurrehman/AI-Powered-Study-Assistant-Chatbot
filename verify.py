"""
Verification script to confirm code structure and basic functionality.
This doesn't require actual PDFs or API keys.
"""
import sys


def verify_imports():
    """Verify all required modules can be imported."""
    print("Verifying imports...")
    
    try:
        from document_processor import DocumentProcessor
        print("  ✓ document_processor")
    except Exception as e:
        print(f"  ✗ document_processor: {e}")
        return False
    
    try:
        from vector_store import VectorStoreManager
        print("  ✓ vector_store")
    except Exception as e:
        print(f"  ✗ vector_store: {e}")
        return False
    
    try:
        from qa_system import QASystem
        print("  ✓ qa_system")
    except Exception as e:
        print(f"  ✗ qa_system: {e}")
        return False
    
    try:
        import main
        print("  ✓ main")
    except Exception as e:
        print(f"  ✗ main: {e}")
        return False
    
    return True


def verify_classes():
    """Verify classes can be instantiated."""
    print("\nVerifying class instantiation...")
    
    try:
        from document_processor import DocumentProcessor
        processor = DocumentProcessor()
        print("  ✓ DocumentProcessor created")
    except Exception as e:
        print(f"  ✗ DocumentProcessor: {e}")
        return False
    
    # Note: VectorStoreManager and QASystem require network access or API keys
    # so we just verify they can be imported
    print("  ✓ Other classes are importable")
    
    return True


def verify_structure():
    """Verify the code structure and design."""
    print("\nVerifying code structure...")
    
    from document_processor import DocumentProcessor
    from vector_store import VectorStoreManager
    from qa_system import QASystem
    
    # Check DocumentProcessor has expected methods
    assert hasattr(DocumentProcessor, 'load_pdf'), "Missing load_pdf method"
    assert hasattr(DocumentProcessor, 'chunk_documents'), "Missing chunk_documents method"
    assert hasattr(DocumentProcessor, 'process_pdf'), "Missing process_pdf method"
    print("  ✓ DocumentProcessor has required methods")
    
    # Check VectorStoreManager has expected methods
    assert hasattr(VectorStoreManager, 'add_documents'), "Missing add_documents method"
    assert hasattr(VectorStoreManager, 'similarity_search'), "Missing similarity_search method"
    assert hasattr(VectorStoreManager, 'similarity_search_with_score'), "Missing similarity_search_with_score method"
    print("  ✓ VectorStoreManager has required methods")
    
    # Check QASystem has expected methods
    assert hasattr(QASystem, 'ask_question'), "Missing ask_question method"
    assert hasattr(QASystem, 'format_response'), "Missing format_response method"
    print("  ✓ QASystem has required methods")
    
    return True


def main():
    """Run verification checks."""
    print("="*80)
    print("AI-Powered Study Assistant - Code Verification")
    print("="*80)
    print()
    
    checks = [
        ("Import verification", verify_imports),
        ("Class instantiation", verify_classes),
        ("Structure verification", verify_structure),
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append(result)
        except Exception as e:
            print(f"\n✗ {name} failed with error: {e}")
            results.append(False)
    
    print("\n" + "="*80)
    if all(results):
        print("✓ All verification checks passed!")
        print("\nThe application structure is correct and ready to use.")
        print("\nNext steps:")
        print("1. Set up your OpenAI API key in .env file")
        print("2. Run: python main.py")
        print("3. Upload PDF documents and start asking questions!")
    else:
        print("✗ Some verification checks failed")
        sys.exit(1)
    print("="*80)


if __name__ == "__main__":
    main()
