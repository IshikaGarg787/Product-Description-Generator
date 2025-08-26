import requests
import logging
from config import Config

logger = logging.getLogger(__name__)

class ProductService:
    def __init__(self):
        self.api_url = Config.DEMO_STORE_API_URL  # Points to GitHub raw JSON

    def fetch_products(self):
        """Fetch products from GitHub JSON"""
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            
            # If JSON is a dictionary with a key 'products', use it
            if isinstance(data, dict) and "products" in data:
                return data["products"]
            return data  # Otherwise, assume JSON is a list of products
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching products: {str(e)}")
            return self._get_sample_products()

    def fetch_product_by_id(self, product_id):
        """Fetch single product by ID from the JSON"""
        products = self.fetch_products()
        for product in products:
            if product.get("id") == product_id:
                return product
        logger.warning(f"Product with ID {product_id} not found")
        return None

    def _get_sample_products(self):
        """Return sample products if API fails"""
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
