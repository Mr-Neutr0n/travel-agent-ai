from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import os
from typing import Dict, Any

class TravelGuidePDFGenerator:
    def __init__(self, destination: str, output_dir: str = "travel_guides"):
        self.destination = destination
        self.output_dir = output_dir
        self.styles = getSampleStyleSheet()
        self._create_custom_styles()
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
    
    def _create_custom_styles(self):
        """Create custom styles for the travel guide"""
        # Title style
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.darkblue,
            alignment=TA_CENTER,
            spaceAfter=30
        )
        
        # Section header style
        self.section_style = ParagraphStyle(
            'SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.darkgreen,
            spaceBefore=20,
            spaceAfter=12,
            leftIndent=0
        )
        
        # Subsection style
        self.subsection_style = ParagraphStyle(
            'SubsectionHeader',
            parent=self.styles['Heading3'],
            fontSize=14,
            textColor=colors.darkred,
            spaceBefore=15,
            spaceAfter=8
        )
        
        # Body text style
        self.body_style = ParagraphStyle(
            'CustomBody',
            parent=self.styles['Normal'],
            fontSize=11,
            alignment=TA_JUSTIFY,
            spaceAfter=6
        )
        
        # Bullet point style
        self.bullet_style = ParagraphStyle(
            'BulletPoint',
            parent=self.styles['Normal'],
            fontSize=10,
            leftIndent=20,
            bulletIndent=10,
            spaceAfter=4
        )
    
    def generate_travel_guide(self, travel_data: Dict[str, Any]) -> str:
        """Generate a comprehensive travel guide PDF"""
        filename = f"{self.destination.replace(' ', '_').replace(',', '')}_Travel_Guide_{datetime.now().strftime('%Y%m%d')}.pdf"
        filepath = os.path.join(self.output_dir, filename)
        
        doc = SimpleDocTemplate(
            filepath,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        story = []
        
        # Title page
        story.extend(self._create_title_page())
        story.append(PageBreak())
        
        # Table of contents would go here in a more advanced version
        
        # Executive summary
        if 'travel_summary' in travel_data:
            story.extend(self._create_executive_summary(travel_data['travel_summary']))
        
        # Hotels section
        if 'validated_hotels' in travel_data:
            story.extend(self._create_hotels_section(travel_data['validated_hotels']))
        
        # Restaurants section  
        if 'validated_restaurants' in travel_data:
            story.extend(self._create_restaurants_section(travel_data['validated_restaurants']))
        
        # Activities section
        if 'validated_activities' in travel_data:
            story.extend(self._create_activities_section(travel_data['validated_activities']))
        
        # Footer with generation info
        story.extend(self._create_footer())
        
        doc.build(story)
        return filepath
    
    def _create_title_page(self):
        """Create the title page"""
        story = []
        
        # Main title
        title = f"🌍 Travel Guide to {self.destination}"
        story.append(Paragraph(title, self.title_style))
        story.append(Spacer(1, 50))
        
        # Subtitle
        subtitle = "Your AI-Powered Travel Companion"
        story.append(Paragraph(subtitle, self.styles['Heading3']))
        story.append(Spacer(1, 30))
        
        # Generation date
        date_text = f"Generated on {datetime.now().strftime('%B %d, %Y')}"
        story.append(Paragraph(date_text, self.styles['Normal']))
        story.append(Spacer(1, 100))
        
        # Description
        description = """
        This comprehensive travel guide has been created by our AI travel planning system 
        to help you make the most of your visit. Inside you'll find carefully curated 
        recommendations for accommodations, dining, and activities, all organized by 
        price range and category to suit your preferences and budget.
        """
        story.append(Paragraph(description, self.body_style))
        
        return story
    
    def _create_executive_summary(self, summary: str):
        """Create executive summary section"""
        story = []
        story.append(Paragraph("📋 Executive Summary", self.section_style))
        story.append(Paragraph(summary, self.body_style))
        story.append(Spacer(1, 20))
        return story
    
    def _create_hotels_section(self, hotels_data):
        """Create hotels section"""
        story = []
        story.append(Paragraph("🏨 Accommodation Recommendations", self.section_style))
        
        # Location notes
        if hasattr(hotels_data, 'location_notes') and hotels_data.location_notes:
            story.append(Paragraph("📍 Best Areas to Stay", self.subsection_style))
            story.append(Paragraph(hotels_data.location_notes, self.body_style))
            story.append(Spacer(1, 15))
        
        # Budget hotels
        if hasattr(hotels_data, 'budget_hotels') and hotels_data.budget_hotels:
            story.extend(self._create_hotel_category("💰 Budget Hotels (Under $100/night)", hotels_data.budget_hotels))
        
        # Mid-range hotels
        if hasattr(hotels_data, 'midrange_hotels') and hotels_data.midrange_hotels:
            story.extend(self._create_hotel_category("🏨 Mid-Range Hotels ($100-250/night)", hotels_data.midrange_hotels))
        
        # Luxury hotels
        if hasattr(hotels_data, 'luxury_hotels') and hotels_data.luxury_hotels:
            story.extend(self._create_hotel_category("✨ Luxury Hotels ($250+/night)", hotels_data.luxury_hotels))
        
        return story
    
    def _create_hotel_category(self, title: str, hotels):
        """Create a hotel category section"""
        story = []
        story.append(Paragraph(title, self.subsection_style))
        
        for hotel in hotels:
            hotel_info = f"""
            <b>{hotel.name}</b><br/>
            <i>Price Range:</i> {hotel.price_per_night}<br/>
            <i>Location:</i> {hotel.location}<br/>
            {hotel.description}
            """
            story.append(Paragraph(hotel_info, self.body_style))
            story.append(Spacer(1, 10))
        
        story.append(Spacer(1, 15))
        return story
    
    def _create_restaurants_section(self, restaurants_data):
        """Create restaurants section"""
        story = []
        story.append(Paragraph("🍽️ Dining Recommendations", self.section_style))
        
        # Local specialties
        if hasattr(restaurants_data, 'local_specialties') and restaurants_data.local_specialties:
            story.append(Paragraph("🥘 Local Specialties & Must-Try Dishes", self.subsection_style))
            for specialty in restaurants_data.local_specialties:
                story.append(Paragraph(f"• {specialty}", self.bullet_style))
            story.append(Spacer(1, 15))
        
        # Budget dining
        if hasattr(restaurants_data, 'budget_dining') and restaurants_data.budget_dining:
            story.extend(self._create_restaurant_category("💰 Budget Dining (Under $25/person)", restaurants_data.budget_dining))
        
        # Mid-range dining
        if hasattr(restaurants_data, 'midrange_dining') and restaurants_data.midrange_dining:
            story.extend(self._create_restaurant_category("🍴 Mid-Range Dining ($25-60/person)", restaurants_data.midrange_dining))
        
        # Fine dining
        if hasattr(restaurants_data, 'fine_dining') and restaurants_data.fine_dining:
            story.extend(self._create_restaurant_category("🥂 Fine Dining ($60+/person)", restaurants_data.fine_dining))
        
        # Unique experiences
        if hasattr(restaurants_data, 'unique_experiences') and restaurants_data.unique_experiences:
            story.append(Paragraph("🌟 Unique Dining Experiences", self.subsection_style))
            for experience in restaurants_data.unique_experiences:
                story.append(Paragraph(f"• {experience}", self.bullet_style))
            story.append(Spacer(1, 15))
        
        return story
    
    def _create_restaurant_category(self, title: str, restaurants):
        """Create a restaurant category section"""
        story = []
        story.append(Paragraph(title, self.subsection_style))
        
        for restaurant in restaurants:
            restaurant_info = f"""
            <b>{restaurant.name}</b> - <i>{restaurant.cuisine_type}</i><br/>
            <i>Price Range:</i> {restaurant.price_per_person}<br/>
            <i>Signature Dishes:</i> {restaurant.signature_dishes}<br/>
            <i>Location:</i> {restaurant.location_notes}
            """
            story.append(Paragraph(restaurant_info, self.body_style))
            story.append(Spacer(1, 10))
        
        story.append(Spacer(1, 15))
        return story
    
    def _create_activities_section(self, activities_data):
        """Create activities section"""
        story = []
        story.append(Paragraph("🎯 Activities & Attractions", self.section_style))
        
        # Must-see attractions
        if hasattr(activities_data, 'must_see_attractions') and activities_data.must_see_attractions:
            story.extend(self._create_activity_category("⭐ Must-See Attractions", activities_data.must_see_attractions))
        
        # Cultural experiences
        if hasattr(activities_data, 'cultural_experiences') and activities_data.cultural_experiences:
            story.extend(self._create_activity_category("🏛️ Cultural Experiences", activities_data.cultural_experiences))
        
        # Outdoor activities
        if hasattr(activities_data, 'outdoor_activities') and activities_data.outdoor_activities:
            story.extend(self._create_activity_category("🌲 Outdoor Activities", activities_data.outdoor_activities))
        
        # Entertainment & nightlife
        if hasattr(activities_data, 'entertainment_nightlife') and activities_data.entertainment_nightlife:
            story.extend(self._create_activity_category("🎭 Entertainment & Nightlife", activities_data.entertainment_nightlife))
        
        # Local experiences
        if hasattr(activities_data, 'local_experiences') and activities_data.local_experiences:
            story.extend(self._create_activity_category("🏠 Local Experiences", activities_data.local_experiences))
        
        # Practical tips
        if hasattr(activities_data, 'practical_tips') and activities_data.practical_tips:
            story.append(Paragraph("💡 Practical Tips", self.subsection_style))
            story.append(Paragraph(activities_data.practical_tips, self.body_style))
            story.append(Spacer(1, 15))
        
        return story
    
    def _create_activity_category(self, title: str, activities):
        """Create an activity category section"""
        story = []
        story.append(Paragraph(title, self.subsection_style))
        
        for activity in activities:
            activity_info = f"""
            <b>{activity.name}</b> - <i>{activity.category}</i><br/>
            <i>Cost:</i> {activity.cost_range}<br/>
            {activity.description}<br/>
            <i>Practical Info:</i> {activity.practical_info}
            """
            story.append(Paragraph(activity_info, self.body_style))
            story.append(Spacer(1, 10))
        
        story.append(Spacer(1, 15))
        return story
    
    def _create_footer(self):
        """Create footer with generation info"""
        story = []
        story.append(PageBreak())
        story.append(Spacer(1, 200))
        
        footer_text = f"""
        <i>This travel guide was generated by Travel Agent AI on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}.<br/>
        Information is subject to change. Please verify details before making reservations.<br/>
        Have an amazing trip to {self.destination}! 🌟</i>
        """
        story.append(Paragraph(footer_text, self.styles['Normal']))
        
        return story 