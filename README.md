# E-commerce Product Description Generator

A comprehensive system that uses AI to generate SEO-optimized product descriptions for e-commerce platforms. Built with Streamlit frontend, Flask backend, and Google's Gemini API.

## 🚀 Features

- **AI-Powered Content Generation**: Uses Google's Gemini API for intelligent product descriptions
- **SEO Optimization**: Generates SEO-friendly titles, meta descriptions, and keyword suggestions
- **Product Data Integration**: Fetches product data from demo store APIs
- **Interactive UI**: Modern Streamlit interface with real-time preview
- **Export Functionality**: Download generated content as JSON or text files
- **Customizable Generation**: Multiple tone, length, and audience options
- **Image Processing**: Automatic image analysis and alt-text generation

## 📁 Project Structure
ecommerce-product-generator/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── gemini_service.py
│   │   └── product_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── image_processor.py
│   └── requirements.txt
├── frontend/
│   ├── streamlit_app.py
│   ├── requirements.txt
│   └── components/
│       ├── __init__.py
│       └── ui_components.py
├── data/
│   └── sample_products.json
├── .env.example
└── README.md

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get it here](https://makersuite.google.com/app/apikey))
- Internet connection for product data fetching

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd ecommerce-product-generator
