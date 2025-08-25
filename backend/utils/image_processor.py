import requests
from PIL import Image
import io
import base64
import logging

logger = logging.getLogger(__name__)

class ImageProcessor:
    """Utility class for processing product images"""
    
    @staticmethod
    def download_image(image_url, max_size=(800, 800)):
        """
        Download and process image from URL
        
        Args:
            image_url (str): URL of the image to download
            max_size (tuple): Maximum size for image resizing
            
        Returns:
            PIL.Image or None: Processed image or None if failed
        """
        try:
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()
            
            # Open image
            image = Image.open(io.BytesIO(response.content))
            
            # Convert to RGB if needed
            if image.mode in ('RGBA', 'P'):
                image = image.convert('RGB')
            
            # Resize if too large
            if image.size[0] > max_size[0] or image.size[1] > max_size[1]:
                image.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            return image
            
        except Exception as e:
            logger.error(f"Error processing image from {image_url}: {str(e)}")
            return None
    
    @staticmethod
    def image_to_base64(image):
        """
        Convert PIL Image to base64 string
        
        Args:
            image (PIL.Image): Image to convert
            
        Returns:
            str: Base64 encoded image string
        """
        try:
            buffer = io.BytesIO()
            image.save(buffer, format='JPEG')
            img_str = base64.b64encode(buffer.getvalue()).decode()
            return f"data:image/jpeg;base64,{img_str}"
        except Exception as e:
            logger.error(f"Error converting image to base64: {str(e)}")
            return None
    
    @staticmethod
    def get_image_info(image_url):
        """
        Get basic information about an image
        
        Args:
            image_url (str): URL of the image
            
        Returns:
            dict: Image information or None if failed
        """
        try:
            image = ImageProcessor.download_image(image_url)
            if image:
                return {
                    "url": image_url,
                    "size": image.size,
                    "format": image.format,
                    "mode": image.mode
                }
            return None
        except Exception as e:
            logger.error(f"Error getting image info: {str(e)}")
            return None