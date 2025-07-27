from dotenv import load_dotenv
load_dotenv()
from google.adk.agents import Agent
from .agent import root_agent
from .pdf_generator import TravelGuidePDFGenerator
import os

class InteractiveTravelAgent:
    """
    Interactive wrapper for the travel agent that includes PDF generation capability
    """
    
    def __init__(self):
        self.travel_agent = root_agent
    
    def plan_trip(self, destination: str) -> dict:
        """
        Plan a trip for the given destination and optionally generate a PDF
        """
        print(f"🌍 Planning your trip to {destination}...")
        print("🔍 Searching for hotels, restaurants, and activities...")
        
        # Run the main travel planning system
        result = self.travel_agent.run(destination)
        
        # Display the summary to the user
        print("\n" + "="*60)
        print("📋 TRAVEL SUMMARY")
        print("="*60)
        print(result.get('travel_summary', 'Summary not available'))
        print("="*60)
        
        # Ask user if they want a PDF
        pdf_choice = self._ask_for_pdf()
        
        if pdf_choice:
            pdf_path = self._generate_pdf(destination, result)
            print(f"\n✅ PDF travel guide generated: {pdf_path}")
            result['pdf_path'] = pdf_path
        
        return result
    
    def _ask_for_pdf(self) -> bool:
        """
        Ask the user if they want to generate a PDF travel guide
        """
        print("\n📄 Would you like to generate a comprehensive PDF travel guide?")
        print("   This will include all recommendations, details, and practical information.")
        
        while True:
            choice = input("\n   Generate PDF? (y/n): ").lower().strip()
            if choice in ['y', 'yes', 'yeah', '1', 'true']:
                return True
            elif choice in ['n', 'no', 'nope', '0', 'false']:
                return False
            else:
                print("   Please enter 'y' for yes or 'n' for no.")
    
    def _generate_pdf(self, destination: str, travel_data: dict) -> str:
        """
        Generate a PDF travel guide using the travel data
        """
        print("\n📝 Generating your personalized PDF travel guide...")
        
        try:
            # Create PDF generator
            pdf_generator = TravelGuidePDFGenerator(destination)
            
            # Generate the PDF
            pdf_path = pdf_generator.generate_travel_guide(travel_data)
            
            print("✨ PDF generation complete!")
            return pdf_path
            
        except Exception as e:
            print(f"❌ Error generating PDF: {str(e)}")
            print("   The travel information is still available above.")
            return None

# Create a PDF generation agent for the workflow
pdf_generation_agent = Agent(
    name="PDFGenerationAgent",
    model="gemini-2.0-flash",
    description="Agent that handles PDF generation and user interaction for travel guides",
    instruction="""
    You are a helpful assistant that manages PDF generation for travel guides.
    
    TASK: After receiving travel planning results, offer to create a PDF travel guide.
    
    WORKFLOW:
    1. Present the travel summary to the user
    2. Ask if they want a comprehensive PDF travel guide
    3. If yes, generate a beautifully formatted PDF with all the travel information
    4. Provide the PDF file path to the user
    
    INTERACTION STYLE:
    - Be enthusiastic about travel planning
    - Clearly explain the value of the PDF guide
    - Be helpful if there are any technical issues
    - Make the user excited about their upcoming trip
    
    PDF BENEFITS TO MENTION:
    - Offline access to all recommendations
    - Professional format for sharing with travel companions
    - Easy reference while traveling
    - Includes all detailed information in organized sections
    """,
    output_key="pdf_interaction_result",
)

def run_interactive_travel_planning(destination: str):
    """
    Main function to run the interactive travel planning with PDF option
    """
    agent = InteractiveTravelAgent()
    return agent.plan_trip(destination)

# Simple CLI for testing
if __name__ == "__main__":
    print("🌟 Welcome to Travel Agent AI!")
    print("=" * 50)
    
    while True:
        destination = input("\n🌍 Where would you like to go? (or 'quit' to exit): ").strip()
        
        if destination.lower() in ['quit', 'exit', 'q', 'bye']:
            print("✈️ Safe travels! See you next time!")
            break
        
        if destination:
            try:
                result = run_interactive_travel_planning(destination)
                print(f"\n🎉 Trip planning complete for {destination}!")
                
                if 'pdf_path' in result:
                    print(f"📚 Your travel guide: {result['pdf_path']}")
                
            except Exception as e:
                print(f"❌ Error: {str(e)}")
                print("Please try again with a different destination.")
        else:
            print("Please enter a valid destination.") 