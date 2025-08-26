import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    FLASK_PORT = int(os.getenv('FLASK_PORT', 5000))
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    
    # Demo store API (using a mock API for demo)
    DEMO_STORE_API_URL = os.getenv('DEMO_STORE_API_URL', "https://fakestoreapi.com/products")
