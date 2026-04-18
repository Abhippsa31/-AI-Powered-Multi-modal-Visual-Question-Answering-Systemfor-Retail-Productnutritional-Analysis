#  AI-Powered Multi-modal Visual Question Answering Systemfor Retail Productnutritional Analysis

An AI-powered computer vision system that analyzes packaged food products using image captioning, OCR, and visual question answering (VQA).  

The system evaluates food healthiness, extracts label text, compares products, answers user questions, and generates voice explanations.

---

# 📌 Overview

Smart Food Product VQA is a deep learning–based application that combines:

- 🧠 Vision-Language Models (BLIP)
- 🔎 Optical Character Recognition (EasyOCR)
- 📊 Rule-based Health Scoring
- 🗣 Text-to-Speech Output
- 🌐 Gradio Web Interface

Users can upload one or two food product images and receive:

- Automatic product description
- Extracted label text
- Health score & classification
- Advantages and disadvantages
- Possible side effects
- Recommended consumption frequency
- Better alternatives
- Product comparison
- Audio explanation
- Answers to custom questions

---

# 🚀 Key Features

## 1️⃣ Image Captioning
Uses BLIP Image Captioning to generate a natural language description of the uploaded food product.

## 2️⃣ OCR Label Extraction
Extracts visible text (ingredients, nutrition labels, brand info) from product packaging using EasyOCR.

## 3️⃣ Health Analysis Engine
A rule-based scoring system analyzes extracted ingredients and classifies products as:

- Natural / Healthy 🌱
- Processed / Junk ❌

Each product receives a health score.

## 4️⃣ Visual Question Answering (VQA)
Users can ask questions like:
- “Is it safe for kids?”
- “Does it contain sugar?”
- “Is this chocolate?”

The BLIP VQA model provides contextual answers based on the image.

## 5️⃣ Product Comparison
When two images are uploaded, the system:
- Compares health scores
- Determines which product is healthier
- Provides a final verdict

## 6️⃣ Voice Output
The complete analysis is converted into speech using gTTS.

---

# 🧠 Models & Technologies Used

## 🔹 BLIP (Bootstrapped Language Image Pretraining)
- Model: `Salesforce/blip-image-captioning-base`
- Model: `Salesforce/blip-vqa-base`
- Framework: HuggingFace Transformers

Used for:
- Image Captioning
- Visual Question Answering

## 🔹 EasyOCR
Used for:
- Extracting ingredient lists
- Reading packaging labels

## 🔹 PyTorch
Deep learning framework powering BLIP models.

## 🔹 Gradio
Provides interactive web interface.

## 🔹 gTTS
Converts generated analysis into audio format.

---

# 🏗 System Architecture

```
User Upload Image
        ↓
BLIP Captioning → Product Description
        ↓
EasyOCR → Extract Label Text
        ↓
Health Analysis Engine
        ↓
Optional VQA Module
        ↓
Comparison Engine (if 2 products)
        ↓
Text-to-Speech Output
        ↓
Gradio Web Interface
```

---

# 📂 Project Structure

```
smart-food-vqa/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/smart-food-vqa.git
cd smart-food-vqa
```

## 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

```bash
python app.py
```

After running:

- A Gradio interface will launch
- Open the provided local URL in your browser
- Upload one or two food images
- Optionally ask a question
- View analysis and listen to audio output

---

# 📊 Health Scoring Logic

The health analysis module checks for keywords such as:

- sugar
- oil
- salt
- chocolate
- cream
- butter
- preservatives

If unhealthy ingredients are detected:
- Product is classified as Processed / Junk
- Score ≈ 40

Otherwise:
- Classified as Natural / Healthy
- Score ≈ 85

This scoring system is rule-based and can be expanded into a machine learning nutritional classifier.

---

# 💻 Hardware Requirements

Minimum:
- 8GB RAM
- CPU support

Recommended:
- NVIDIA GPU with CUDA for faster inference

The application automatically detects CUDA availability.

---

# 📦 Dependencies

Main libraries:

- torch
- transformers
- gradio
- Pillow
- gTTS
- easyocr
- numpy

All dependencies are listed in `requirements.txt`.

---

# 🔐 Limitations

- Health scoring is rule-based, not medically certified
- OCR accuracy depends on image clarity
- No real nutritional database integration
- Does not calculate exact calories or macros
- VQA answers depend on model inference quality

This system is for educational and research purposes only.

---

# 🔮 Future Improvements

- Integrate USDA nutritional database
- Calorie & macronutrient estimation
- Barcode scanning support
- Multi-language OCR support
- Deep learning–based nutrition classifier
- Cloud deployment (HuggingFace / AWS)
- Mobile app integration
- Personalized diet recommendations

---

# 🌍 Use Cases

- Consumer awareness tool
- Educational AI project
- Health-tech prototype
- Computer Vision portfolio project
- AI-based product comparison system

---

# ⭐ Support

If you find this project useful, consider starring the repository.
