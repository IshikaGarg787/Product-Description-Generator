from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from config import Config
from services.gemini_service import GeminiService
from services.product_service import ProductService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Initialize services
gemini_service = GeminiService(Config.GEMINI_API_KEY)
product_service = ProductService()

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "E-commerce Product Generator"})

@app.route('/api/products', methods=['GET'])
def get_products():
    """Get products from demo store API"""
    try:
        products = product_service.fetch_products()
        return jsonify({"success": True, "data": products})
    except Exception as e:
        logger.error(f"Error fetching products: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/generate-description', methods=['POST'])
def generate_description():
    """Generate product description using Gemini API"""
    try:
        data = request.json
        product_data = data.get('product_data')
        category = data.get('category', 'general')
        
        if not product_data:
            return jsonify({"success": False, "error": "Product data is required"}), 400
        
        # Generate description using Gemini
        result = gemini_service.generate_product_description(product_data, category)
        
        return jsonify({"success": True, "data": result})
    
    except Exception as e:
        logger.error(f"Error generating description: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/optimize-seo', methods=['POST'])
def optimize_seo():
    """Optimize product content for SEO"""
    try:
        data = request.json
        content = data.get('content')
        keywords = data.get('keywords', [])
        
        if not content:
            return jsonify({"success": False, "error": "Content is required"}), 400
        
        optimized_content = gemini_service.optimize_for_seo(content, keywords)
        
        return jsonify({"success": True, "data": optimized_content})
    
    except Exception as e:
        logger.error(f"Error optimizing SEO: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.FLASK_PORT, host='0.0.0.0')
