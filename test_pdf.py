#!/usr/bin/env python3
"""
Test script for PDF generation functionality
"""

from travel_agent.pdf_generator import TravelGuidePDFGenerator
from pydantic import BaseModel
from typing import List

# Mock data structures for testing (matching the agent.py schemas)
class Hotel(BaseModel):
    name: str
    price_range: str
    price_per_night: str
    description: str
    location: str

class HotelOptions(BaseModel):
    budget_hotels: List[Hotel]
    midrange_hotels: List[Hotel]
    luxury_hotels: List[Hotel]
    location_notes: str

class Restaurant(BaseModel):
    name: str
    cuisine_type: str
    price_range: str
    price_per_person: str
    signature_dishes: str
    location_notes: str

class RestaurantOptions(BaseModel):
    local_specialties: List[str]
    budget_dining: List[Restaurant]
    midrange_dining: List[Restaurant]
    fine_dining: List[Restaurant]
    unique_experiences: List[str]

class Activity(BaseModel):
    name: str
    category: str
    description: str
    cost_range: str
    practical_info: str

class ActivityOptions(BaseModel):
    must_see_attractions: List[Activity]
    cultural_experiences: List[Activity]
    outdoor_activities: List[Activity]
    entertainment_nightlife: List[Activity]
    local_experiences: List[Activity]
    practical_tips: str

def create_sample_data():
    """Create sample travel data for testing"""
    
    # Sample hotels
    hotels = HotelOptions(
        budget_hotels=[
            Hotel(
                name="Budget Stay Central",
                price_range="Budget",
                price_per_night="$50-80/night",
                description="Clean, modern hostel in the heart of the city with shared and private rooms. Free WiFi and breakfast included.",
                location="City Center, walking distance to main attractions"
            ),
            Hotel(
                name="Backpacker's Paradise",
                price_range="Budget", 
                price_per_night="$40-70/night",
                description="Popular hostel with social atmosphere, kitchen facilities, and organized tours.",
                location="Historic District, near public transportation"
            )
        ],
        midrange_hotels=[
            Hotel(
                name="Boutique Hotel Charm",
                price_range="Mid-range",
                price_per_night="$120-180/night", 
                description="Stylish boutique hotel with locally-inspired decor, rooftop terrace, and excellent service.",
                location="Trendy neighborhood with restaurants and cafes"
            ),
            Hotel(
                name="Business Hotel Plus",
                price_range="Mid-range",
                price_per_night="$100-150/night",
                description="Modern business hotel with fitness center, conference rooms, and 24/7 room service.",
                location="Business district, metro access"
            )
        ],
        luxury_hotels=[
            Hotel(
                name="Grand Palace Hotel",
                price_range="Luxury",
                price_per_night="$300-500/night",
                description="Historic luxury hotel with spa, fine dining, concierge service, and panoramic city views.",
                location="Premium location overlooking the main square"
            )
        ],
        location_notes="The city center offers the best access to attractions. The historic district has character but can be noisy. Business district is quiet but less scenic."
    )
    
    # Sample restaurants
    restaurants = RestaurantOptions(
        local_specialties=[
            "Traditional Local Stew - hearty dish with local vegetables and meat",
            "Street Food Markets - authentic snacks and quick bites",
            "Regional Cheese Platter - selection of local artisanal cheeses"
        ],
        budget_dining=[
            Restaurant(
                name="Local Bites Cafe",
                cuisine_type="Local/Traditional",
                price_range="Budget",
                price_per_person="$8-15",
                signature_dishes="Traditional stew, homemade bread, local coffee",
                location_notes="Cozy family-run cafe in residential area"
            ),
            Restaurant(
                name="Street Food Central",
                cuisine_type="Various/Street Food", 
                price_range="Budget",
                price_per_person="$5-12",
                signature_dishes="Local sandwiches, fresh fruit, grilled meats",
                location_notes="Bustling market area, authentic atmosphere"
            )
        ],
        midrange_dining=[
            Restaurant(
                name="Farm to Table Restaurant",
                cuisine_type="Modern Local",
                price_range="Mid-range",
                price_per_person="$25-40",
                signature_dishes="Seasonal vegetables, locally-sourced meat, craft cocktails",
                location_notes="Trendy area with outdoor seating"
            )
        ],
        fine_dining=[
            Restaurant(
                name="Chef's Table Experience",
                cuisine_type="Fine Dining/Fusion",
                price_range="Fine Dining",
                price_per_person="$80-120",
                signature_dishes="Tasting menu, wine pairings, molecular gastronomy",
                location_notes="Upscale district, reservations required"
            )
        ],
        unique_experiences=[
            "Cooking class with local chef",
            "Food tour of historic markets",
            "Wine tasting at local vineyard"
        ]
    )
    
    # Sample activities
    activities = ActivityOptions(
        must_see_attractions=[
            Activity(
                name="Historic Cathedral",
                category="Attraction",
                description="Stunning 12th-century cathedral with guided tours and climbing tower",
                cost_range="$10-15 entrance",
                practical_info="Open 9am-6pm, tours every hour, 200 steps to tower"
            ),
            Activity(
                name="National Museum",
                category="Attraction", 
                description="World-class collection of local art and historical artifacts",
                cost_range="$12 entrance, free on Sundays",
                practical_info="Closed Mondays, audio guide included"
            )
        ],
        cultural_experiences=[
            Activity(
                name="Traditional Craft Workshop",
                category="Cultural",
                description="Learn traditional pottery or weaving from local artisans",
                cost_range="$30-50 per session",
                practical_info="Book 24 hours in advance, 2-hour sessions"
            )
        ],
        outdoor_activities=[
            Activity(
                name="City Park Walking Trail",
                category="Outdoor",
                description="Scenic 3-mile trail through the largest city park with lake views",
                cost_range="Free",
                practical_info="Best in morning or evening, bike rentals available"
            )
        ],
        entertainment_nightlife=[
            Activity(
                name="Local Music Venue",
                category="Entertainment",
                description="Intimate venue featuring local and touring musicians",
                cost_range="$15-25 cover charge",
                practical_info="Shows start at 9pm, advance tickets recommended"
            )
        ],
        local_experiences=[
            Activity(
                name="Morning Market Tour",
                category="Local",
                description="Guided tour of the bustling morning market with tastings",
                cost_range="$20 per person",
                practical_info="Starts 7am, includes breakfast, bring comfortable shoes"
            )
        ],
        practical_tips="Many attractions offer city passes for discounts. Public transport is efficient and affordable. Summer is peak season with longer hours but larger crowds."
    )
    
    # Complete travel data
    travel_data = {
        'validated_hotels': hotels,
        'validated_restaurants': restaurants,
        'validated_activities': activities,
        'travel_summary': """
        🏨 **ACCOMMODATION HIGHLIGHTS**
        - Budget: Budget Stay Central - Modern hostel with free breakfast ($50-80/night)
        - Mid-range: Boutique Hotel Charm - Stylish with rooftop terrace ($120-180/night)
        - Luxury: Grand Palace Hotel - Historic luxury with spa and city views ($300-500/night)

        🍽️ **DINING HIGHLIGHTS**
        - Local Bites Cafe - Traditional stew and homemade bread ($8-15/person)
        - Farm to Table Restaurant - Seasonal local cuisine ($25-40/person)
        - Chef's Table Experience - Fine dining tasting menu ($80-120/person)
        - Must-try: Traditional local stew, street food markets, regional cheese

        🎯 **TOP ACTIVITIES**
        - Historic Cathedral - 12th-century architecture with tower climb ($10-15)
        - National Museum - World-class art collection (free on Sundays)
        - Morning Market Tour - Authentic local experience with tastings ($20)
        - City Park Walking Trail - Scenic 3-mile trail (free)

        📝 **QUICK TIPS**
        - City center offers best access to attractions
        - Many attractions offer discounted city passes
        - Public transport is efficient and affordable
        - Summer is peak season with longer hours but larger crowds
        """
    }
    
    return travel_data

def test_pdf_generation():
    """Test the PDF generation functionality"""
    print("🧪 Testing PDF Generation...")
    
    # Create sample data
    travel_data = create_sample_data()
    destination = "Sample City, Test Country"
    
    try:
        # Initialize PDF generator
        pdf_generator = TravelGuidePDFGenerator(destination)
        
        # Generate PDF
        pdf_path = pdf_generator.generate_travel_guide(travel_data)
        
        print(f"✅ PDF generated successfully: {pdf_path}")
        print(f"📁 Check the 'travel_guides' directory for your PDF")
        
        return pdf_path
        
    except Exception as e:
        print(f"❌ Error generating PDF: {str(e)}")
        return None

if __name__ == "__main__":
    print("🌟 Travel Agent AI - PDF Generation Test")
    print("=" * 50)
    
    test_pdf_generation()
    
    print("\n🎉 Test complete!")
    print("If successful, you should see a PDF file in the travel_guides directory.") 