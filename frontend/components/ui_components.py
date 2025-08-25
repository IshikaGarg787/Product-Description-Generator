import streamlit as st
import requests
from PIL import Image
import io
import pandas as pd

class ProductCard:
    """Reusable product card component"""
    
    @staticmethod
    def render(product, show_details=True):
        """
        Render a product card
        
        Args:
            product (dict): Product data
            show_details (bool): Whether to show detailed information
        """
        container = st.container()
        
        with container:
            col1, col2 = st.columns([1, 2] if show_details else [1, 3])
            
            with col1:
                ProductCard._render_image(product.get('image', ''))
            
            with col2:
                ProductCard._render_info(product, show_details)
    
    @staticmethod
    def _render_image(image_url):
        """Render product image"""
        try:
            if image_url:
                response = requests.get(image_url, timeout=10)
                if response.status_code == 200:
                    image = Image.open(io.BytesIO(response.content))
                    st.image(image, use_column_width=True)
                    return
        except Exception:
            pass
        
        # Fallback placeholder
        st.markdown("""
            <div style='
                width: 100%; 
                height: 200px; 
                background: #f0f0f0; 
                display: flex; 
                align-items: center; 
                justify-content: center;
                border-radius: 8px;
                color: #888;
            '>
                🖼️ No Image Available
            </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def _render_info(product, show_details):
        """Render product information"""
        st.subheader(product.get('title', 'Unknown Product'))
        
        # Price and basic info
        price = product.get('price', 0)
        st.markdown(f"**💰 Price:** ${price:.2f}")
        
        category = product.get('category', 'Unknown').title()
        st.markdown(f"**📁 Category:** {category}")
        
        # Rating
        rating = product.get('rating', {})
        if rating:
            rate = rating.get('rate', 0)
            count = rating.get('count', 0)
            stars = '⭐' * int(rate)
            st.markdown(f"**⭐ Rating:** {rate}/5 {stars} ({count} reviews)")
        
        if show_details:
            # Description
            description = product.get('description', '')
            if description:
                with st.expander("📄 Original Description"):
                    st.write(description)

class SEOMetrics:
    """Component for displaying SEO metrics and analysis"""
    
    @staticmethod
    def render(content):
        """
        Render SEO metrics for content
        
        Args:
            content (dict): Generated content with SEO data
        """
        st.subheader("📊 SEO Analysis")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            SEOMetrics._title_analysis(content.get('seo_title', ''))
        
        with col2:
            SEOMetrics._description_analysis(content.get('description', ''))
        
        with col3:
            SEOMetrics._keywords_analysis(content.get('keywords', []))
    
    @staticmethod
    def _title_analysis(title):
        """Analyze SEO title"""
        title_len = len(title)
        
        st.metric(
            label="Title Length",
            value=f"{title_len} chars",
            delta=f"{60 - title_len} from ideal" if title_len < 60 else f"{title_len - 60} over limit"
        )
        
        if title_len <= 60:
            st.success("✅ Good length")
        else:
            st.warning("⚠️ Too long for SEO")
    
    @staticmethod
    def _description_analysis(description):
        """Analyze description"""
        desc_len = len(description)
        word_count = len(description.split())
        
        st.metric(
            label="Description",
            value=f"{word_count} words",
            delta=f"{desc_len} characters"
        )
        
        if 150 <= word_count <= 300:
            st.success("✅ Good length")
        elif word_count < 150:
            st.warning("⚠️ Too short")
        else:
            st.info("ℹ️ Consider shorter")
    
    @staticmethod
    def _keywords_analysis(keywords):
        """Analyze keywords"""
        keyword_count = len(keywords)
        
        st.metric(
            label="Keywords",
            value=f"{keyword_count} tags",
            delta="SEO optimized" if 5 <= keyword_count <= 10 else "Review needed"
        )
        
        if 5 <= keyword_count <= 10:
            st.success("✅ Good count")
        else:
            st.warning("⚠️ Adjust count")

class GenerationControls:
    """Component for generation controls and options"""
    
    @staticmethod
    def render():
        """Render generation controls"""
        st.subheader("🎛️ Generation Settings")
        
        with st.expander("⚙️ Advanced Options"):
            col1, col2 = st.columns(2)
            
            with col1:
                tone = st.selectbox(
                    "Writing Tone:",
                    ["Professional", "Casual", "Enthusiastic", "Technical", "Luxury"],
                    key="writing_tone"
                )
                
                length = st.selectbox(
                    "Description Length:",
                    ["Short (100-150 words)", "Medium (150-250 words)", "Long (250+ words)"],
                    index=1,
                    key="desc_length"
                )
            
            with col2:
                focus_keywords = st.text_input(
                    "Focus Keywords (comma-separated):",
                    placeholder="e.g., premium, quality, durable",
                    key="focus_keywords"
                )
                
                target_audience = st.selectbox(
                    "Target Audience:",
                    ["General", "Budget-conscious", "Premium buyers", "Tech enthusiasts", "Fashion-forward"],
                    key="target_audience"
                )
            
            include_specs = st.checkbox("Include Technical Specifications", value=True)
            include_benefits = st.checkbox("Emphasize Benefits over Features", value=True)
            include_cta = st.checkbox("Include Call-to-Action", value=True)
            
            return {
                "tone": tone,
                "length": length,
                "focus_keywords": [k.strip() for k in focus_keywords.split(',') if k.strip()],
                "target_audience": target_audience,
                "include_specs": include_specs,
                "include_benefits": include_benefits,
                "include_cta": include_cta
            }