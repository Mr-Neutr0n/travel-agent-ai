"""
Travel Agent AI Package

A comprehensive travel planning system using Google's Agent Development Kit (ADK)
that provides AI-powered recommendations for accommodations, dining, and activities.
"""

from .agent import root_agent, parallel_search_agent, summary_agent
from .pdf_generator import TravelGuidePDFGenerator
from .interactive_agent import InteractiveTravelAgent, run_interactive_travel_planning

__version__ = "1.0.0"
__author__ = "Travel Agent AI Team"

__all__ = [
    'root_agent',
    'parallel_search_agent', 
    'summary_agent',
    'TravelGuidePDFGenerator',
    'InteractiveTravelAgent',
    'run_interactive_travel_planning'
] 