# 🚚 Delivery Delay Prediction with XGBoost + Streamlit Dashboard

A machine learning project that predicts whether an order will be delivered late based on a real-world supply chain dataset. Includes an automated ML pipeline and an interactive Streamlit app for live predictions.

---

## 📊 Project Overview

This project was built to solve a classification problem using the Dataco Smart Supply Chain dataset (~180K records, 50+ features). We used XGBoost for modeling and deployed an interactive dashboard using Streamlit.

---

## 🧠 Key Features

- ✅ Full pipeline: data cleaning → training → evaluation → dashboard
- ✅ Automated with modular scripts (`run_all.py`)
- ✅ Streamlit web app for real-time CSV upload & prediction
- ✅ Uses a sample CSV for deployment demo (<25MB GitHub limit)
- ✅ Ready to scale or plug into APIs, dashboards, or cron jobs

---

## 🛠️ Tech Stack

- **Python 3.10**
- **Pandas** & **NumPy**
- **Scikit-learn**
- **XGBoost**
- **Joblib** (model saving)
- **Streamlit** (interactive app)

---

## 📁 Project Structure
delivery_delays_project/
├── data/
│ └── sample_data.csv # sample for demo
├── model/
│ └── delivery_model.pkl # trained XGBoost model
├── notebooks/
│ └── Delivery_Delays_XGBoost.ipynb
├── app.py # Streamlit app
├── run_all.py # One-click pipeline runner
├── train_model.py
├── evaluate.py
├── load_data.py
├── preprocess.py
├── requirements.txt
├── README.md
└── .streamlit/
  └── config.toml # optional layout config

---

## 📁 Dataset

- **Source**: [Dataco Smart Supply Chain (Kaggle)](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)  
- **Size**: 180,519 rows × 53 columns  
- **Includes**: order details, shipping info, customer & product data, geography, and sales.
- ⚠️ **Note**: This app uses a 1,000-row sample to demonstrate functionality.

---

## 🧠 How to Use

### 1. 🔁 Retrain the model (optional)

```python
python run_all.py
```

This script will:
- Load + clean the data
- Train the model
- Evaluate accuracy & F1 score
- Save the model to model/delivery_model.pkl

### 1. 2. 🎯 Run the Streamlit App

```python
streamlit run app.py
```

Then open your browser at http://localhost:8501.
Upload a CSV with the same structure as the training data to get predictions.

---

## 🌍 Streamlit Cloud (Demo Link)
👉 [Try the app here (hosted on Streamlit Cloud)] (https://late-delivery-risk.streamlit.app/)

## 📌 Author
Novita Triwidianingsih
📫 [LinkedIn](https://www.linkedin.com/in/novitatrw94/) | 💻 [GitHub](https://github.com/Novitatrw30/my_portfolio/)
