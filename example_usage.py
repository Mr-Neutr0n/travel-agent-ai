#!/usr/bin/env python3
"""
Example usage of Travel Agent AI with PDF generation
"""

from travel_agent.interactive_agent import run_interactive_travel_planning
from travel_agent.pdf_generator import TravelGuidePDFGenerator

def simple_example():
    """Simple example of using the travel agent"""
    print("🌟 Travel Agent AI - Simple Example")
    print("=" * 50)
    
    # Example 1: Interactive mode (will prompt user for PDF)
    print("\n📍 Example 1: Interactive Planning")
    print("This will prompt you to generate a PDF after showing the summary:")
    
    destination = "Kyoto, Japan"
    result = run_interactive_travel_planning(destination)
    
    if 'pdf_path' in result:
        print(f"✅ PDF created: {result['pdf_path']}")
    
    print("\n🎉 Example complete!")

def programmatic_example():
    """Example of programmatic PDF generation without user prompts"""
    print("\n📍 Example 2: Programmatic PDF Generation")
    print("(This would require running the full agent system)")
    
    # Note: This is a conceptual example - you'd need to run the actual agents
    # and have proper API keys configured for Google ADK
    
    destination = "Barcelona, Spain"
    print(f"Would plan trip to {destination} and generate PDF automatically")
    
    # Example of how you could generate a PDF programmatically:
    # result = root_agent.run(destination)
    # pdf_generator = TravelGuidePDFGenerator(destination)
    # pdf_path = pdf_generator.generate_travel_guide(result)

if __name__ == "__main__":
    print("🚀 Choose an example:")
    print("1. Interactive mode (includes user prompts)")
    print("2. Show programmatic approach")
    print("3. Test PDF generation only")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        simple_example()
    elif choice == "2":
        programmatic_example()
    elif choice == "3":
        print("\n🧪 Running PDF test...")
        import subprocess
        subprocess.run(["python", "test_pdf.py"])
    else:
        print("Invalid choice. Running PDF test instead.")
        import subprocess
        subprocess.run(["python", "test_pdf.py"]) 