# 📦 Supply Chain Late Delivery Risk Prediction

A complete Machine Learning + Streamlit project to predict whether an order will be delivered **on time** or **late** using historical supply chain data.

---

## ⭐ Project Overview

This project uses a real-world **DataCo Supply Chain Dataset** to:

* Clean and preprocess order data
* Engineer powerful shipment and product features
* Train advanced ML models (XGBoost & Random Forest)
* Evaluate model performance using ROC-AUC, Precision, Recall & F1
* Build an interactive **Streamlit application** for real-time predictions

The final model predicts:

* **🟢 Likely On-Time Delivery**
* **🔴 High Late Delivery Risk**

---

## 📸 Output Screenshot

Below is the prediction output captured from the Streamlit app:

![Streamlit Prediction Output](output_screenshot.png)

> *(Replace `output_screenshot.png` with your actual uploaded image filename in the repo.)*
> (Add your output screenshot image here)

Example:

```
🟢 Likely On-Time Delivery
📉 Delay Probability: 0.33
```

---

## 🚀 Features

### ✔ Machine Learning Pipeline

* XGBoost & Random Forest Training
* Automatic Feature Engineering
* Class Imbalance Handling
* Cross Validation & AUC Scoring

### ✔ Streamlit UI

* Clean and modern interface
* Easy 7-field input form
* Auto-engineered ML features
* Styled prediction cards (green/red)

---

## 📁 Project Structure

```
Predicting-Delivery-Delays-in-Supply-Chain/
│── app.py                     # Streamlit Application
│── app_compare.py            # Styled Streamlit version
│── README.md                 # Project Documentation
│── DataCoSupplyChainDataset.csv
│── models_fixed/
│     ├── best_model.pkl
│     ├── xgb_model.pkl
│     ├── rf_model.pkl
│     ├── feature_list.txt
│     ├── model_metadata.json
│     ├── xgboost_feature_importance.png
│     ├── randomforest_feature_importance.png
│     ├── roc_curves.png
│── notebooks/
│     ├── OnTime_Delivery_Project_CLEAN.ipynb
```

---

## 🧠 How the Model Works

The app automatically calculates:

* Order time features
* Shipment urgency
* Discount flags
* Price-per-item
* Month/Weekday/Quarter
* Weekend & business hour features

This reduces manual input and increases prediction accuracy.

---

## ▶️ Running the Streamlit App

### 1️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run the App

```
streamlit run app.py
```

### 3️⃣ Open in Browser

```
http://localhost:8501
```

---

## 📈 Model Performance

* XGBoost AUC: (example) 0.89
* RandomForest AUC: (example) 0.85
* Best model saved: **XGBoost / RandomForest**

Actual numbers appear in `model_metadata.json`.

---

## 📤 Future Enhancements

* CSV Batch Prediction Upload
* SHAP Explainability (Why prediction happened)
* Dashboard with charts
* Automated PDF Report

---

## 👨‍💻 Author

**S.V Murali**

* Machine Learning & Data Science Projects
* Python | SQL | Streamlit | ML Engineering

---

## ⭐ Give the Project a Star!

If you found this project useful, please ⭐ the repository on GitHub.

---
