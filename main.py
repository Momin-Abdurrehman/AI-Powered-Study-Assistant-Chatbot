"""
AI-Powered Study Assistant Chatbot
Main application entry point.
"""
import os
import sys
from dotenv import load_dotenv
from document_processor import DocumentProcessor
from vector_store import VectorStoreManager
from qa_system import QASystem


class StudyAssistant:
    """Main study assistant application."""
    
    def __init__(self):
        """Initialize the study assistant."""
        # Load environment variables
        load_dotenv()
        
        # Initialize components
        self.doc_processor = DocumentProcessor()
        self.vector_store = VectorStoreManager()
        self.qa_system = None
        self.uploaded_files = []
    
    def upload_pdf(self, pdf_path: str) -> bool:
        """
        Upload and process a PDF file.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            True if successful, False otherwise
        """
        try:
            print(f"\nProcessing PDF: {pdf_path}")
            
            # Process the PDF
            chunks = self.doc_processor.process_pdf(pdf_path)
            print(f"Created {len(chunks)} text chunks from the document")
            
            # Add to vector store
            self.vector_store.add_documents(chunks)
            print(f"Added document to knowledge base")
            
            # Track uploaded file
            self.uploaded_files.append(pdf_path)
            
            # Initialize QA system if not already done
            if self.qa_system is None:
                self.qa_system = QASystem(self.vector_store)
            
            return True
        except Exception as e:
            print(f"Error uploading PDF: {e}")
            return False
    
    def ask_question(self, question: str) -> None:
        """
        Ask a question about uploaded documents.
        
        Args:
            question: The question to ask
        """
        if self.qa_system is None:
            print("\nPlease upload at least one PDF document first!")
            return
        
        try:
            print("\nSearching for relevant information...")
            response = self.qa_system.ask_question(question)
            formatted_response = self.qa_system.format_response(response)
            print(formatted_response)
        except Exception as e:
            print(f"Error answering question: {e}")
    
    def list_documents(self) -> None:
        """List all uploaded documents."""
        if not self.uploaded_files:
            print("\nNo documents uploaded yet.")
        else:
            print("\nUploaded documents:")
            for i, file_path in enumerate(self.uploaded_files, 1):
                print(f"  {i}. {os.path.basename(file_path)}")
    
    def clear_knowledge_base(self) -> None:
        """Clear all uploaded documents."""
        try:
            self.vector_store.clear()
            self.uploaded_files = []
            self.qa_system = None
            print("\nKnowledge base cleared successfully!")
        except Exception as e:
            print(f"Error clearing knowledge base: {e}")
    
    def run(self) -> None:
        """Run the interactive chatbot interface."""
        print("="*80)
        print("AI-Powered Study Assistant Chatbot")
        print("="*80)
        print("\nWelcome! This chatbot helps you study by answering questions about your course")
        print("materials with citations from uploaded PDFs.")
        print("\nCommands:")
        print("  upload <path>  - Upload a PDF file")
        print("  ask <question> - Ask a question about uploaded materials")
        print("  list          - List all uploaded documents")
        print("  clear         - Clear all uploaded documents")
        print("  help          - Show this help message")
        print("  quit          - Exit the application")
        print("="*80)
        
        while True:
            try:
                user_input = input("\n> ").strip()
                
                if not user_input:
                    continue
                
                # Parse command
                parts = user_input.split(maxsplit=1)
                command = parts[0].lower()
                args = parts[1] if len(parts) > 1 else ""
                
                if command == "quit" or command == "exit":
                    print("\nThank you for using the Study Assistant. Goodbye!")
                    break
                
                elif command == "help":
                    print("\nCommands:")
                    print("  upload <path>  - Upload a PDF file")
                    print("  ask <question> - Ask a question about uploaded materials")
                    print("  list          - List all uploaded documents")
                    print("  clear         - Clear all uploaded documents")
                    print("  help          - Show this help message")
                    print("  quit          - Exit the application")
                
                elif command == "upload":
                    if not args:
                        print("Please provide a PDF file path: upload <path>")
                    else:
                        self.upload_pdf(args)
                
                elif command == "ask":
                    if not args:
                        print("Please provide a question: ask <question>")
                    else:
                        self.ask_question(args)
                
                elif command == "list":
                    self.list_documents()
                
                elif command == "clear":
                    confirm = input("Are you sure you want to clear all documents? (yes/no): ")
                    if confirm.lower() == "yes":
                        self.clear_knowledge_base()
                
                else:
                    print(f"Unknown command: {command}. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\n\nInterrupted. Type 'quit' to exit.")
            except Exception as e:
                print(f"\nError: {e}")


def main():
    """Main entry point."""
    # Check for OpenAI API key
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found!")
        print("\nPlease set your OpenAI API key:")
        print("1. Copy .env.example to .env")
        print("2. Edit .env and add your OpenAI API key")
        print("3. Run the application again")
        sys.exit(1)
    
    # Create and run the assistant
    assistant = StudyAssistant()
    assistant.run()


if __name__ == "__main__":
    main()
