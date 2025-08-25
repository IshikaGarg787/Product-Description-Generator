"""
Services package for the e-commerce product generator backend.
Contains business logic and external API integrations.
"""

__version__ = "1.0.0"
__author__ = "E-commerce Product Generator"

# Import main services for easy access
from .gemini_service import GeminiService
from .product_service import ProductService

__all__ = ['GeminiService', 'ProductService']