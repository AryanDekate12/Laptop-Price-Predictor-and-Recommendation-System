# 💻 Laptop Price Predictor and Recommendation System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

An **AI-powered laptop price prediction and recommendation system** built using Machine Learning and Streamlit.

The system predicts laptop prices based on hardware specifications and also recommends the best laptops under a selected budget.

---

# 🎥 Project Demo



https://github.com/user-attachments/assets/bf43cbf5-1219-4df1-9af4-8de4916aa7ca


---

# 🚀 Features

- Laptop price prediction using Machine Learning
- Automatic specification detection when selecting a laptop model
- Editable laptop configuration (RAM, SSD, CPU, GPU, etc.)
- Budget-based laptop recommendation system
- Interactive Streamlit web application
- Synthetic dataset generation for realistic laptop configurations

---

# 🧠 Machine Learning Model

This project uses **Random Forest Regressor** for predicting laptop prices.

### Input Features

- Brand
- CPU
- GPU
- RAM
- SSD
- HDD
- Screen Size
- Weight
- Operating System

### Output

- Estimated Laptop Price

---

# 🏗️ System Architecture

```
User Input
   │
   ▼
Streamlit Web Application
   │
   ▼
Feature Processing
   │
   ▼
Machine Learning Model
(Random Forest Regressor)
   │
   ▼
Price Prediction
   │
   ▼
Laptop Recommendation System
```

---

# 📂 Project Structure

```
Laptop-Price-Predictor-ML
│
├── app.py
├── generate_dataset.py
├── model_training.ipynb
├── dataset.csv
├── model.pkl
├── encoders.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📄 File Description

| File | Description |
|-----|-------------|
| app.py | Streamlit web application |
| generate_dataset.py | Generates synthetic laptop dataset |
| model_training.ipynb | Machine learning model training |
| dataset.csv | Laptop dataset |
| model.pkl | Trained ML model |
| encoders.pkl | Label encoders used in training |
| scaler.pkl | Feature scaling object |
| requirements.txt | Python dependencies |

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/AryanDekate12/Laptop-Price-Predictor-ML.git
```

### 2️⃣ Navigate to project folder

```
cd Laptop-Price-Predictor-ML
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the application

```
streamlit run app.py
```

---

# 📊 Example Use Case

User selects:

Brand → Dell  
Model → XPS 13  

The system automatically detects:

- CPU → i7
- RAM → 16GB
- SSD → 512GB

User modifies configuration:

RAM → 32GB  
SSD → 1TB  

The AI predicts the **updated laptop price**.

---

# 💰 Budget Recommendation System

Users can select a budget range to find laptops offering the best value.

Example:

Budget: ₹60,000

Recommended laptops:

- Lenovo IdeaPad Slim 3
- HP Pavilion 15
- Acer Aspire Lite

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

# 🔮 Future Improvements

Possible upgrades for the project:

- Integration with real laptop datasets
- Laptop comparison tool
- Laptop image preview
- Natural language AI laptop advisor
- Cloud deployment

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project.

---

# 👨‍💻 Author

Aryan Dekate

GitHub: https://github.com/AryanDekate12

---

⭐ If you found this project helpful, please consider **starring the repository**.
