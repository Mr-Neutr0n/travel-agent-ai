# Travel Agent AI 🌍✈️

An intelligent travel planning system built with Google's Agent Development Kit (ADK) that provides comprehensive destination research across accommodations, dining, and activities.

## 🚀 Features

- **Multi-Agent Architecture**: Parallel processing of travel research across multiple domains
- **Comprehensive Search**: Simultaneous research of hotels, restaurants, and activities
- **Structured Output**: Validates and organizes results using Pydantic schemas
- **Price-Categorized Recommendations**: Budget, mid-range, and luxury options for all categories
- **Intelligent Summarization**: Creates concise, actionable travel summaries

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

## 📋 Prerequisites

- Python 3.8+
- Google ADK access
- Environment variables configured (see `.env.example`)

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

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

## 💻 Usage

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

## 📖 Example Output

The system provides structured recommendations like:

**🏨 ACCOMMODATION HIGHLIGHTS**
- Budget: Hostel recommendations with key amenities
- Mid-range: Boutique hotels with location advantages
- Luxury: Premium hotels with exceptional services

**🍽️ DINING HIGHLIGHTS**
- Local specialties and where to find them
- Price-categorized restaurant recommendations
- Signature dishes and unique experiences

**🎯 TOP ACTIVITIES**
- Must-see attractions with practical info
- Cultural experiences and local insights
- Outdoor activities and entertainment options

## 🔧 Configuration

The system can be customized by modifying agent instructions in `travel-agent/agent.py`:

- Search criteria and keywords
- Output formatting preferences
- Price range categorizations
- Number of recommendations per category

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