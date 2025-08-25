import requests
import logging
from config import Config

logger = logging.getLogger(__name__)

class ProductService:
    def __init__(self):
        self.api_url = Config.DEMO_STORE_API_URL
    
    def fetch_products(self, limit=20):
        """Fetch products from demo store API"""
        try:
            response = requests.get(f"{self.api_url}?limit={limit}")
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching products: {str(e)}")
            # Return sample data if API fails
            return self._get_sample_products()
    
    def fetch_product_by_id(self, product_id):
        """Fetch single product by ID"""
        try:
            response = requests.get(f"{self.api_url}/{product_id}")
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching product {product_id}: {str(e)}")
            return None
    
    def _get_sample_products(self):
        """Return sample products if API is unavailable"""
        return [
            {
                "id": 1,
                "title": "Sample Product 1",
                "price": 29.99,
                "description": "This is a sample product description",
                "category": "electronics",
                "image": "https://via.placeholder.com/300",
                "rating": {"rate": 4.5, "count": 100}
            },
            {
                "id": 2,
                "title": "Sample Product 2",
                "price": 49.99,
                "description": "Another sample product description",
                "category": "clothing",
                "image": "https://via.placeholder.com/300",
                "rating": {"rate": 4.2, "count": 85}
            }
        ]