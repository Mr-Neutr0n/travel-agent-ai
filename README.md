# Travel Agent AI 🌍✈️

An intelligent travel planning system built with Google's Agent Development Kit (ADK) that provides comprehensive destination research across accommodations, dining, and activities.

## 🚀 Features

- **Multi-Agent Architecture**: Parallel processing of travel research across multiple domains
- **Comprehensive Search**: Simultaneous research of hotels, restaurants, and activities
- **Structured Output**: Validates and organizes results using Pydantic schemas
- **Price-Categorized Recommendations**: Budget, mid-range, and luxury options for all categories
- **Intelligent Summarization**: Creates concise, actionable travel summaries
- **📄 PDF Travel Guides**: Generate beautiful, professional PDF travel guides with all recommendations
- **Smart Fallback System**: Tries real AI agents first, falls back to destination-specific demo data
- **Destination-Specific Content**: London, Barcelona, Paris get unique recommendations even in demo mode

## 🏗️ Architecture

The system uses a sophisticated multi-agent architecture:

### Core Agents
- **Hotel Search Agent**: Finds accommodation options across all price ranges
- **Restaurant Search Agent**: Discovers dining options and local specialties
- **Activities Search Agent**: Identifies attractions, cultural experiences, and activities

### Validation Layer
- **Hotel Validation Agent**: Structures hotel data with price categorization
- **Restaurant Validation Agent**: Organizes dining options by cuisine and price
- **Activities Validation Agent**: Categorizes activities by type and experience level

### Orchestration
- **Parallel Search System**: Runs all research agents simultaneously for efficiency
- **Summary Agent**: Creates concise travel recommendations from structured data
- **Root Agent**: Coordinates the entire travel planning workflow

## 🏨 Data Structure

### Hotel Information
- Budget hotels (under $100/night)
- Mid-range hotels ($100-250/night)
- Luxury hotels ($250+/night)
- Location and neighborhood insights

### Restaurant Information
- Local cuisine specialties
- Budget dining (under $25/person)
- Mid-range dining ($25-60/person)
- Fine dining ($60+/person)
- Unique dining experiences

### Activity Information
- Must-see attractions
- Cultural experiences
- Outdoor activities
- Entertainment and nightlife
- Authentic local experiences
- Practical booking and timing information

## 🛠️ Technology Stack

- **Framework**: Google Agent Development Kit (ADK)
- **Language**: Python
- **Data Validation**: Pydantic
- **Search**: Google Search integration
- **Model**: Gemini 2.0 Flash
- **PDF Generation**: ReportLab

## 📋 Prerequisites

- Python 3.8+
- Google ADK access (optional - system works in demo mode without API keys)
- Environment variables configured (see `env.example`)

### For Full AI Functionality
To use real AI-powered research instead of demo mode:
1. Set up Google ADK API keys
2. Configure environment variables
3. Ensure proper authentication

### Demo Mode
Without API keys, the system provides:
- Destination-specific recommendations for major cities
- Realistic hotel, restaurant, and activity suggestions
- Full PDF generation functionality

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/travel-agent-ai.git
cd travel-agent-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Set up environment variables for full AI functionality:
```bash
cp env.example .env
# Edit .env with your Google ADK API keys
```

4. Test the system:
```bash
# Try interactive mode (works without API keys)
python -m travel_agent.interactive_agent

# Test PDF generation
python test_pdf.py
```

## 💻 Usage

### Basic Usage
```python
from travel_agent.agent import root_agent

# Run travel planning for any destination
result = root_agent.run("Paris, France")

# Access structured results
hotels = result["validated_hotels"]
restaurants = result["validated_restaurants"] 
activities = result["validated_activities"]
summary = result["travel_summary"]
```

### Interactive Mode with PDF Generation
```python
from travel_agent.interactive_agent import run_interactive_travel_planning

# Interactive planning with PDF option
result = run_interactive_travel_planning("Tokyo, Japan")

# User will be prompted to generate a PDF after seeing the summary
if 'pdf_path' in result:
    print(f"PDF guide saved to: {result['pdf_path']}")
```

### Command Line Interface
```bash
cd travel-agent-ai
python -m travel_agent.interactive_agent
```

### Quick Examples
```bash
# Test PDF generation with sample data
python test_pdf.py

# Example usage patterns
python example_usage.py
```

## 📖 Example Output

### For London:
**🏨 ACCOMMODATION HIGHLIGHTS**
- Budget: Premier Inn, YHA hostels (£60-100/night)
- Mid-range: Boutique hotels in Covent Garden (£150-250/night)
- Luxury: The Ritz, Savoy Hotel (£400+/night)

**🍽️ DINING HIGHLIGHTS**
- Traditional: Fish & chips, Sunday roast, afternoon tea
- Markets: Borough Market, Camden Market
- Fine dining: Michelin-starred restaurants in Mayfair

**🎯 TOP ACTIVITIES**
- Must-see: Big Ben, Tower of London, British Museum
- Cultural: West End shows, Tate Modern
- Royal parks: Hyde Park, Regent's Park

### For Barcelona:
**🏨 ACCOMMODATION HIGHLIGHTS**
- Budget: Generator Hostel, Sant Jordi hostels (€30-70/night)
- Mid-range: Boutique hotels in Eixample (€100-180/night)
- Luxury: Hotel Casa Sagnier, W Barcelona (€300+/night)

**🍽️ DINING HIGHLIGHTS**
- Tapas: Patatas bravas, jamón ibérico, pintxos
- Paella: Traditional Valencian or seafood versions
- Markets: La Boquería, Sant Antoni Market

**🎯 TOP ACTIVITIES**
- Gaudí architecture: Sagrada Família, Park Güell, Casa Batlló
- Beaches: Barceloneta, Nova Icària
- Gothic Quarter: Cathedral, Picasso Museum

## 📄 PDF Travel Guides

The system can generate professional PDF travel guides with the following features:

### PDF Contents
- **Title Page**: Destination name and generation date
- **Executive Summary**: Concise overview of top recommendations
- **Hotel Section**: Categorized by budget, mid-range, and luxury with detailed descriptions
- **Restaurant Section**: Local specialties and dining options by price range
- **Activities Section**: Must-see attractions, cultural experiences, and local activities
- **Practical Information**: Tips, booking info, and insider recommendations

### PDF Features
- **Professional Layout**: Clean, organized design with color-coded sections
- **Comprehensive Details**: All search results structured and formatted
- **Offline Access**: Perfect for travel without internet connection
- **Shareable Format**: Easy to share with travel companions
- **Print-Ready**: High-quality formatting for physical copies

### Generating PDFs
1. Run the interactive travel agent: `python -m travel_agent.interactive_agent`
2. Enter any destination (London, Barcelona, Paris, etc.)
3. Review your personalized travel summary
4. When prompted: "Generate PDF? (y/n)" - type 'y'
5. PDF will be saved in the `travel_guides/` directory with timestamp

### PDF Examples Generated
- `london_Travel_Guide_20250728.pdf`
- `barcelona_spain_Travel_Guide_20250728.pdf`
- `paris_france_Travel_Guide_20250728.pdf`

## 🔧 Configuration

### Agent Configuration
The system can be customized by modifying agent instructions in `travel_agent/agent.py`:
- Search criteria and keywords
- Output formatting preferences
- Price range categorizations
- Number of recommendations per category

### Demo Mode Configuration
Destination-specific content can be customized in `travel_agent/interactive_agent.py`:
- Add new destinations to `_get_destination_specific_content()`
- Customize hotel, restaurant, and activity recommendations
- Update pricing and local tips

### Environment Variables
```bash
# Google ADK Configuration (optional)
GOOGLE_ADK_API_KEY=your_api_key_here

# Optional: Disable OpenTelemetry
OTEL_PYTHON_DISABLED=true
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Agent Development Kit team
- Pydantic for data validation
- The travel and hospitality industry for inspiration

## 🐛 Issues

If you encounter any issues or have suggestions, please [create an issue](https://github.com/yourusername/travel-agent-ai/issues) on GitHub.

---

**Happy travels! 🌟** 