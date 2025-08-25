import google.generativeai as genai
import json
import logging

logger = logging.getLogger(__name__)

class GeminiService:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    
    def generate_product_description(self, product_data, category="general"):
        """Generate comprehensive product description"""
        try:
            prompt = self._create_description_prompt(product_data, category)
            response = self.model.generate_content(prompt)
            
            # Parse the response to extract structured data
            return self._parse_description_response(response.text)
        
        except Exception as e:
            logger.error(f"Error generating description: {str(e)}")
            raise e
    
    def optimize_for_seo(self, content, keywords):
        """Optimize content for SEO"""
        try:
            prompt = f"""
            Optimize the following product content for SEO:
            
            Content: {content}
            Target Keywords: {', '.join(keywords)}
            
            Please provide:
            1. SEO-optimized title (under 60 characters)
            2. Meta description (under 160 characters)
            3. Improved product description with natural keyword integration
            4. Suggested alt text for images
            
            Format as JSON with keys: seo_title, meta_description, optimized_description, alt_text
            """
            
            response = self.model.generate_content(prompt)
            return self._parse_json_response(response.text)
        
        except Exception as e:
            logger.error(f"Error optimizing SEO: {str(e)}")
            raise e
    
    def _create_description_prompt(self, product_data, category):
        """Create prompt for product description generation"""
        return f"""
        Generate a comprehensive e-commerce product description for the following product:
        
        Product Information:
        - Title: {product_data.get('title', 'N/A')}
        - Category: {category}
        - Price: ${product_data.get('price', 'N/A')}
        - Current Description: {product_data.get('description', 'N/A')}
        - Image URL: {product_data.get('image', 'N/A')}
        - Rating: {product_data.get('rating', {}).get('rate', 'N/A')} ({product_data.get('rating', {}).get('count', 'N/A')} reviews)
        
        Please provide:
        1. SEO-optimized product title (compelling and keyword-rich)
        2. Detailed product description (3-4 paragraphs)
        3. Key features (5-7 bullet points)
        4. Technical specifications (if applicable)
        5. Suggested keywords for SEO
        
        Format the response as JSON with keys: 
        seo_title, description, features, specifications, keywords
        
        Make it engaging, informative, and optimized for e-commerce conversion.
        """
    
    def _parse_description_response(self, response_text):
        """Parse and clean the response from Gemini"""
        try:
            # Try to extract JSON from the response
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1
            
            if start_idx != -1 and end_idx != -1:
                json_str = response_text[start_idx:end_idx]
                return json.loads(json_str)
            else:
                # If no JSON found, return structured text
                return {
                    "seo_title": "Generated Product Title",
                    "description": response_text,
                    "features": ["Feature extraction from response"],
                    "specifications": {},
                    "keywords": ["product", "ecommerce"]
                }
        except json.JSONDecodeError:
            return {
                "seo_title": "Generated Product Title",
                "description": response_text,
                "features": ["Unable to parse features"],
                "specifications": {},
                "keywords": ["product"]
            }
    
    def _parse_json_response(self, response_text):
        """Parse JSON response from Gemini"""
        try:
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1
            
            if start_idx != -1 and end_idx != -1:
                json_str = response_text[start_idx:end_idx]
                return json.loads(json_str)
            else:
                return {"error": "Could not parse response"}
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response"}