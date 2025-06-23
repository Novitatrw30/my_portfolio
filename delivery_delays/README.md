# 📦 Predicting Delivery Delays in a Smart Supply Chain using XGBoost

This project builds a machine learning model to predict whether an order will be delivered late using real-world supply chain data. The goal is to help businesses proactively address shipping issues, improve logistics performance, and enhance customer satisfaction.

---

## 🧠 Problem Statement

Shipping delays negatively impact customer experience and operational efficiency. This project aims to classify orders as delayed or on-time based on historical order, customer, and shipping data.

---

## 📁 Dataset

- **Source**: [Dataco Smart Supply Chain (Kaggle)](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)
- **Size**: 180,519 rows × 53 columns
- **Scope**: Includes order details, shipping info, customer & product data, geography, and sales

---

## 🔍 Exploratory Data Analysis (EDA)

- ~57% of orders were delayed
- Standard Class shipping made up 60% of shipments
- "First Class" had a suspicious 100% delay rate → flagged as unreliable
- Delays showed no strong seasonal pattern

---

## 🛠️ Feature Engineering

Created several domain-relevant features:

- `shipping_duration`: Time between order and ship dates
- `order_month`: Extracted from order date
- `Shipping Mode Clean`: Cleaned suspicious categories
- `is_first_class`: Flag for unreliable shipping mode
- One-hot encoded key categorical features

---

## 📈 Modeling

Used **XGBoost Classifier** with hyperparameters:
```python
n_estimators=100,
learning_rate=0.1,
max_depth=6,
scale_pos_weight= class_0 / class_1,
eval_metric='logloss',
use_label_encoder=False,
random_state=42

