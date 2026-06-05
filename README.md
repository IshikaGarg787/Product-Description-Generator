# 🛍️ E-commerce Product Description Generator

An AI-powered web application that generates SEO-optimized product descriptions for e-commerce platforms using Google's Gemini API.

The system helps businesses create engaging product content, SEO metadata, keyword suggestions, and marketing-friendly descriptions automatically through an interactive web interface.

---

## ✨ Features

* 🤖 AI-powered product description generation using Gemini API
* 🔍 SEO-optimized titles and meta descriptions
* 🏷️ Keyword suggestion generation
* 🛒 Product data integration from demo store APIs
* 🖼️ Automatic image analysis & alt-text generation
* 🎛️ Customizable tone, audience, and description length
* 📥 Export generated content as JSON or text files
* ⚡ Real-time preview with interactive UI
* 🌐 Full-stack architecture with Streamlit + Flask

---

## 🛠️ Tech Stack

| Technology | Purpose               |
| ---------- | --------------------- |
| Python     | Core Programming      |
| Flask      | Backend API           |
| Streamlit  | Frontend Interface    |
| Gemini API | AI Content Generation |
| HTML/CSS   | UI Styling            |
| JSON       | Data Handling         |

---

## 📂 Project Structure

```text
ecommerce-product-generator/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   │
│   ├── services/
│   │   ├── gemini_service.py
│   │   └── product_service.py
│   │
│   ├── utils/
│   │   └── image_processor.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── streamlit_app.py
│   │
│   ├── components/
│   │   └── ui_components.py
│   │
│   └── requirements.txt
│
├── data/
│   └── sample_products.json
│
├── .env.example
│
└── README.md
```

---

## 🚀 How It Works

1. User selects or uploads product information
2. Product data is processed through the Flask backend
3. Gemini API generates:

   * Product descriptions
   * SEO titles
   * Meta descriptions
   * Keywords
4. Generated content is displayed in the Streamlit UI
5. User can export results as JSON or text files

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

### 2️⃣ Navigate to Project Directory

```bash
cd ecommerce-product-generator
```

---

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

### 4️⃣ Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

## 🔑 Setup Gemini API Key

Create a `.env` file using `.env.example`

Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Get API key from:
https://makersuite.google.com/app/apikey

---

## 📦 Install Backend Dependencies

```bash
cd backend

pip install -r requirements.txt
```

---

## ▶️ Run Backend Server

```bash
python app.py
```

---

## 📦 Install Frontend Dependencies

```bash
cd frontend

pip install -r requirements.txt
```

---

## ▶️ Run Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

---

## 🌐 Deployed Application

### Backend API

https://product-description-generator-71kn.onrender.com/api/products

---

### Frontend Application

https://product-description-generator-1.onrender.com/

---

## ⭐ Author

ISHIKA GARG
B.Tech CSE (AI & Data Analytics) '28

---

### ⭐ If you like this project

Give this repository a star on GitHub!

