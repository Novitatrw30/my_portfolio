# 📦 Delivery Delays Prediction with XGBoost and Streamlit Dashboard

Predicts whether a product delivery will be delayed using historical supply chain data. Includes automated training pipeline and an interactive Streamlit dashboard.

---

## 🚀 Features
- XGBoost model for binary classification
- Automated pipeline via run_all.py
- Streamlit web app for easy predictions
- Cleaned and encoded real-world dataset

---

## 📁 Dataset

- **Source**: [Dataco Smart Supply Chain (Kaggle)](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)  
- **Size**: 180,519 rows × 53 columns  
- **Includes**: order details, shipping info, customer & product data, geography, and sales.
- ⚠️ **Note**: This app uses a 1,000-row sample to demonstrate functionality.

---

## 🧠 How to Use
1. Run run_all.py to train and evaluate the model.
2. Start the dashboard:

```python
streamlit run app.py
```

3. Upload a CSV with the same structure as the training data to get predictions.

---

## 📦 Tech Stack
- Python
- Pandas, Scikit-learn, XGBoost
- Streamlit for frontend
- Joblib for model saving

---

## 📌 Author
Novita Triwidianingsih
📫 [LinkedIn](https://www.linkedin.com/in/novitatrw94/) | 💻 [GitHub](https://github.com/Novitatrw30/my_portfolio/)
