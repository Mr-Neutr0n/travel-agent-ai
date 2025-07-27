from dotenv import load_dotenv
load_dotenv()

import asyncio
import sys
import os
from pathlib import Path
import uuid

# Fix imports to work both as module and direct execution
try:
    # Try relative imports first (when run as module)
    from .agent import root_agent
    from .pdf_generator import TravelGuidePDFGenerator
except ImportError:
    # Fall back to absolute imports (when run directly)
    # Add the parent directory to Python path
    current_dir = Path(__file__).parent
    parent_dir = current_dir.parent
    sys.path.insert(0, str(parent_dir))
    
    from travel_agent.agent import root_agent
    from travel_agent.pdf_generator import TravelGuidePDFGenerator

# Google ADK imports for proper execution
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

class InteractiveTravelAgent:
    """
    Interactive wrapper for the travel agent that includes PDF generation capability
    """
    
    def __init__(self):
        self.travel_agent = root_agent
        self.session_service = InMemorySessionService()
        self.app_name = "TravelAgentAI"
        self.user_id = "user"
        
    def plan_trip(self, destination: str) -> dict:
        """
        Plan a trip for the given destination and optionally generate a PDF
        """
        print(f"🌍 Planning your trip to {destination}...")
        print("🔍 Searching for hotels, restaurants, and activities...")
        
        try:
            # Try to run the actual Google ADK agents
            result = asyncio.run(self._run_real_agents(destination))
            
            # Display the summary to the user
            self._display_summary(result)
            
            # Ask user if they want a PDF
            pdf_choice = self._ask_for_pdf()
            
            if pdf_choice:
                pdf_path = self._generate_pdf(destination, result)
                if pdf_path:
                    print(f"\n✅ PDF travel guide generated: {pdf_path}")
                    result['pdf_path'] = pdf_path
            
            return result
            
        except Exception as e:
            print(f"❌ Error during trip planning: {str(e)}")
            print("🔄 Falling back to demo mode...")
            
            # Fall back to simulation if agents fail
            result = self._simulate_travel_planning(destination)
            self._display_summary(result)
            
            pdf_choice = self._ask_for_pdf()
            if pdf_choice:
                pdf_path = self._generate_pdf(destination, result)
                if pdf_path:
                    print(f"\n✅ PDF travel guide generated: {pdf_path}")
                    result['pdf_path'] = pdf_path
            
            return result
    
    async def _run_real_agents(self, destination: str) -> dict:
        """
        Execute the actual Google ADK agents with proper session management
        """
        # Create session
        session_id = str(uuid.uuid4())
        await self.session_service.create_session(
            app_name=self.app_name,
            user_id=self.user_id,
            session_id=session_id,
            state={}
        )
        
        # Create runner
        runner = Runner(
            agent=self.travel_agent,
            session_service=self.session_service,
            app_name=self.app_name
        )
        
        # Create message
        message = types.Content(
            role="user",
            parts=[types.Part(text=f"Plan a comprehensive trip to {destination}. Provide detailed recommendations for hotels, restaurants, and activities.")]
        )
        
        # Execute and collect results
        result_data = {}
        final_response = None
        
        print("🤖 AI agents working...")
        
        async for event in runner.run_async(
            user_id=self.user_id,
            session_id=session_id,
            new_message=message
        ):
            # Print progress
            if hasattr(event, 'agent_name') and event.agent_name:
                print(f"   🔄 {event.agent_name} processing...")
            
            # Collect outputs
            if hasattr(event, 'agent_outputs') and event.agent_outputs:
                result_data.update(event.agent_outputs)
            
            # Get final response text
            if event.is_final_response() and event.content and event.content.parts:
                for part in event.content.parts:
                    if hasattr(part, 'text') and part.text:
                        final_response = part.text
                        print(f"   ✅ Complete!")
        
        # If we have structured data, use it; otherwise use the final response text
        if result_data:
            if final_response and 'travel_summary' not in result_data:
                result_data['travel_summary'] = final_response
            return result_data
        else:
            # If no structured data, create from final response
            return {
                'travel_summary': final_response or f"Travel planning completed for {destination}",
                'destination': destination,
                'agent_response': final_response
            }
    
    def _simulate_travel_planning(self, destination: str) -> dict:
        """
        Simulate travel planning results with destination-specific content
        """
        print("📝 Using demo mode with simulated data...")
        
        # Create more realistic destination-specific content
        destination_tips = self._get_destination_specific_content(destination)
        
        return {
            'travel_summary': f"""
🏨 **ACCOMMODATION HIGHLIGHTS for {destination}**
{destination_tips['hotels']}

🍽️ **DINING HIGHLIGHTS**
{destination_tips['food']}

🎯 **TOP ACTIVITIES**
{destination_tips['activities']}

📝 **QUICK TIPS**
{destination_tips['tips']}

✅ Trip planning complete! This is demo data - configure Google ADK API keys for real AI research.
            """.strip(),
            'destination': destination,
            'planning_status': 'simulated'
        }
    
    def _get_destination_specific_content(self, destination: str) -> dict:
        """
        Get destination-specific content for simulation
        """
        dest_lower = destination.lower()
        
        # Basic destination-specific data
        if 'london' in dest_lower:
            return {
                'hotels': "- Budget: Premier Inn, YHA hostels (£60-100/night)\n- Mid-range: Boutique hotels in Covent Garden (£150-250/night)\n- Luxury: The Ritz, Savoy Hotel (£400+/night)",
                'food': "- Traditional: Fish & chips, Sunday roast, afternoon tea\n- Markets: Borough Market, Camden Market\n- Fine dining: Michelin-starred restaurants in Mayfair",
                'activities': "- Must-see: Big Ben, Tower of London, British Museum\n- Cultural: West End shows, Tate Modern\n- Royal parks: Hyde Park, Regent's Park",
                'tips': "- Use Oyster Card for transport\n- Book theatre shows in advance\n- Weather can be unpredictable - bring umbrella\n- Tipping: 10-15% in restaurants"
            }
        elif 'barcelona' in dest_lower or 'spain' in dest_lower:
            return {
                'hotels': "- Budget: Generator Hostel, Sant Jordi hostels (€30-70/night)\n- Mid-range: Boutique hotels in Eixample (€100-180/night)\n- Luxury: Hotel Casa Sagnier, W Barcelona (€300+/night)",
                'food': "- Tapas: Patatas bravas, jamón ibérico, pintxos\n- Paella: Traditional Valencian or seafood versions\n- Markets: La Boquería, Sant Antoni Market",
                'activities': "- Gaudí architecture: Sagrada Família, Park Güell, Casa Batlló\n- Beaches: Barceloneta, Nova Icària\n- Gothic Quarter: Cathedral, Picasso Museum",
                'tips': "- Siesta time: Many shops close 2-5pm\n- Dinner is late: 9-11pm is normal\n- Metro system is efficient and affordable\n- Learn basic Catalan greetings"
            }
        elif 'paris' in dest_lower or 'france' in dest_lower:
            return {
                'hotels': "- Budget: MIJE hostels, Hotel des Jeunes (€50-90/night)\n- Mid-range: Boutique hotels in Le Marais (€120-200/night)\n- Luxury: Le Bristol, Plaza Athénée (€500+/night)",
                'food': "- Classics: Croissants, escargot, coq au vin\n- Bakeries: Fresh baguettes and pastries daily\n- Wine: French wine tasting experiences",
                'activities': "- Icons: Eiffel Tower, Louvre, Notre-Dame\n- Districts: Montmartre, Latin Quarter, Champs-Élysées\n- Day trips: Versailles, Giverny",
                'tips': "- Learn basic French phrases\n- Café culture: sit and people-watch\n- Metro closes around 1am (2am weekends)\n- Tipping: Round up or add small amount"
            }
        else:
            return {
                'hotels': f"- Budget: Hostels and budget hotels (€30-80/night)\n- Mid-range: 3-star hotels and boutique properties (€80-180/night)\n- Luxury: 5-star hotels and resorts (€200+/night)",
                'food': f"- Local specialties and traditional cuisine\n- Street food and market experiences\n- Regional wines and beverages",
                'activities': f"- Historic landmarks and cultural sites\n- Museums and art galleries\n- Local neighborhoods and markets",
                'tips': f"- Research local customs and etiquette\n- Check visa requirements\n- Learn basic local phrases\n- Use local transportation apps"
            }
    
    def _display_summary(self, result: dict):
        """Display the travel summary to the user"""
        print("\n" + "="*60)
        print("📋 TRAVEL SUMMARY")
        print("="*60)
        
        # Try to find and display the travel summary
        summary_text = None
        
        # Look for summary in various possible keys
        for key in ['travel_summary', 'summary', 'final_summary', 'agent_response']:
            if key in result and result[key]:
                summary_text = result[key]
                break
        
        # If no direct summary, create a basic one
        if not summary_text:
            summary_text = f"Travel planning completed for {result.get('destination', 'your destination')}!"
        
        print(summary_text)
        print("="*60)
    
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
            
            # If we have simulated data, convert it to the format the PDF expects
            if travel_data.get('planning_status') == 'simulated':
                travel_data = self._convert_to_pdf_format(destination, travel_data)
            
            # Generate the PDF
            pdf_path = pdf_generator.generate_travel_guide(travel_data)
            
            print("✨ PDF generation complete!")
            return pdf_path
            
        except Exception as e:
            print(f"❌ Error generating PDF: {str(e)}")
            print("   The travel information is still available above.")
            return None
    
    def _convert_to_pdf_format(self, destination: str, basic_data: dict) -> dict:
        """
        Convert basic travel data to the structured format expected by PDF generator
        """
        from travel_agent.pdf_generator import TravelGuidePDFGenerator
        
        # Use the same sample data structure from test_pdf.py for consistent results
        from test_pdf import create_sample_data
        
        # Get the sample data and customize it for the destination
        sample_data = create_sample_data()
        
        # Update the summary with destination-specific content
        updated_summary = basic_data.get('travel_summary', '').replace('Sample City, Test Country', destination)
        sample_data['travel_summary'] = updated_summary or f"Travel planning complete for {destination}!"
        
        return sample_data

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
    print("🚀 Attempting to use real AI agents...")
    print("📝 Will fall back to enhanced demo mode if agents fail.")
    
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
                    
            except KeyboardInterrupt:
                print("\n\n✈️ Travel planning cancelled. Safe travels!")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}")
                print("Please try again with a different destination.")
        else:
            print("Please enter a valid destination.") 