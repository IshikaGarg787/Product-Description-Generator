import streamlit as st
import requests
import json
import pandas as pd
from PIL import Image
import io

# Configuration
BACKEND_URL = "http://localhost:5001/api"

def init_session_state():
    """Initialize session state variables"""
    if 'products' not in st.session_state:
        st.session_state.products = []
    if 'selected_product' not in st.session_state:
        st.session_state.selected_product = None
    if 'generated_content' not in st.session_state:
        st.session_state.generated_content = None

def fetch_products():
    """Fetch products from backend API"""
    try:
        response = requests.get(f"{BACKEND_URL}/products")
        if response.status_code == 200:
            data = response.json()
            return data.get('data', [])
        else:
            st.error(f"Error fetching products: {response.status_code}")
            return []
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to backend. Make sure Flask server is running on port 5000.")
        return []
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return []

def generate_description(product_data, category):
    """Generate product description using backend API"""
    try:
        payload = {
            "product_data": product_data,
            "category": category
        }
        
        response = requests.post(
            f"{BACKEND_URL}/generate-description",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            return response.json().get('data')
        else:
            st.error(f"Error generating description: {response.status_code}")
            return None
            
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def optimize_seo(content, keywords):
    """Optimize content for SEO"""
    try:
        payload = {
            "content": content,
            "keywords": keywords
        }
        
        response = requests.post(
            f"{BACKEND_URL}/optimize-seo",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            return response.json().get('data')
        else:
            st.error(f"Error optimizing SEO: {response.status_code}")
            return None
            
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def display_product_card(product):
    """Display product information in a card format"""
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            response = requests.get(product['image'])
            if response.status_code == 200:
                image = Image.open(io.BytesIO(response.content))
                st.image(image, use_column_width=True)
        except:
            st.write("🖼️ Image not available")
    
    with col2:
        st.subheader(product['title'])
        st.write(f"**Price:** ${product['price']}")
        st.write(f"**Category:** {product['category']}")
        if 'rating' in product:
            st.write(f"**Rating:** {product['rating']['rate']} ⭐ ({product['rating']['count']} reviews)")
        
        with st.expander("Original Description"):
            st.write(product['description'])

def main():
    st.set_page_config(
        page_title="E-commerce Product Description Generator",
        page_icon="🛍️",
        layout="wide"
    )
    
    init_session_state()
    
    st.title("🛍️ E-commerce Product Description Generator")
    st.markdown("Generate SEO-optimized product descriptions using AI")
    
    # Sidebar
    with st.sidebar:
        st.header("Settings")
        
        # Backend status check
        try:
            health_response = requests.get(f"{BACKEND_URL}/health", timeout=5)
            if health_response.status_code == 200:
                st.success("✅ Backend Connected")
            else:
                st.error("❌ Backend Error")
        except:
            st.error("❌ Backend Offline")
        
        st.markdown("---")
        
        # Load products button
        if st.button("🔄 Load Products", type="primary"):
            with st.spinner("Loading products..."):
                st.session_state.products = fetch_products()
            
            if st.session_state.products:
                st.success(f"Loaded {len(st.session_state.products)} products")
            else:
                st.warning("No products loaded")
    
    # Main content
    if not st.session_state.products:
        st.info("Click 'Load Products' in the sidebar to get started")
        return
    
    # Product selection
    st.header("📦 Select a Product")
    
    product_options = [f"{p['id']}: {p['title'][:50]}..." for p in st.session_state.products]
    selected_idx = st.selectbox(
        "Choose a product:",
        range(len(product_options)),
        format_func=lambda x: product_options[x]
    )
    
    if selected_idx is not None:
        st.session_state.selected_product = st.session_state.products[selected_idx]
    
    if st.session_state.selected_product:
        product = st.session_state.selected_product
        
        st.markdown("---")
        st.header("📋 Product Information")
        display_product_card(product)
        
        # Generation options
        st.markdown("---")
        st.header("🤖 Generate Description")
        
        col1, col2 = st.columns(2)
        
        with col1:
            category = st.selectbox(
                "Product Category:",
                ["electronics", "clothing", "jewelry", "books", "home", "sports", "general"],
                index=6
            )
        
        with col2:
            if st.button("🚀 Generate Description", type="primary"):
                with st.spinner("Generating description..."):
                    result = generate_description(product, category)
                    if result:
                        st.session_state.generated_content = result
                        st.success("Description generated successfully!")
        
        # Display generated content
        if st.session_state.generated_content:
            st.markdown("---")
            st.header("✨ Generated Content")
            
            content = st.session_state.generated_content
            
            # SEO Title
            st.subheader("🏷️ SEO-Optimized Title")
            new_title = st.text_input(
                "Title:",
                value=content.get('seo_title', ''),
                key="seo_title"
            )
            
            # Description
            st.subheader("📝 Product Description")
            new_description = st.text_area(
                "Description:",
                value=content.get('description', ''),
                height=200,
                key="description"
            )
            
            # Features
            if 'features' in content and content['features']:
                st.subheader("⭐ Key Features")
                for i, feature in enumerate(content['features']):
                    st.write(f"• {feature}")
            
            # Keywords
            if 'keywords' in content and content['keywords']:
                st.subheader("🔍 SEO Keywords")
                keywords_str = ', '.join(content['keywords'])
                keywords = st.text_input("Keywords:", value=keywords_str)
            
            # SEO Optimization
            st.markdown("---")
            st.subheader("🎯 SEO Optimization")
            
            if st.button("🔍 Optimize for SEO"):
                if new_description:
                    keyword_list = [k.strip() for k in keywords.split(',') if k.strip()]
                    with st.spinner("Optimizing for SEO..."):
                        seo_result = optimize_seo(new_description, keyword_list)
                        
                        if seo_result and 'error' not in seo_result:
                            st.success("Content optimized for SEO!")
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                st.write("**SEO Title:**")
                                st.code(seo_result.get('seo_title', 'N/A'))
                                
                                st.write("**Meta Description:**")
                                st.code(seo_result.get('meta_description', 'N/A'))
                            
                            with col2:
                                st.write("**Alt Text:**")
                                st.code(seo_result.get('alt_text', 'N/A'))
                                
                                if 'optimized_description' in seo_result:
                                    st.write("**Optimized Description:**")
                                    st.text_area(
                                        "",
                                        value=seo_result['optimized_description'],
                                        height=150,
                                        key="optimized_desc"
                                    )
                        else:
                            st.error("Failed to optimize content")
                else:
                    st.warning("Please generate a description first")
            
            # Export functionality
            st.markdown("---")
            st.subheader("📤 Export")
            
            export_data = {
                "original_product": product,
                "generated_content": st.session_state.generated_content,
                "final_title": new_title,
                "final_description": new_description
            }
            
            st.download_button(
                label="📥 Download as JSON",
                data=json.dumps(export_data, indent=2),
                file_name=f"product_{product['id']}_description.json",
                mime="application/json"
            )

if __name__ == "__main__":
    main()