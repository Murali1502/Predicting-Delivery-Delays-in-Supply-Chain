import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
from datetime import datetime

# Load model
@st.cache_resource
def load_model():
    return pickle.load(open("models_fixed/best_model.pkl", "rb"))

model = load_model()
metadata = json.load(open("models_fixed/model_metadata.json"))
features = metadata["feature_list"]

st.title("📦 Supply Chain Late Delivery Risk Prediction")
st.write("Predict whether an order will be delivered on time or late.")

# ---------------------------------------
# USER INPUTS (ONLY 7 FIELDS)
# ---------------------------------------
st.subheader("Enter Order Details")

order_date = st.date_input("Order Date")
shipping_mode = st.selectbox("Shipping Mode", ["Standard Class", "Second Class", "First Class", "Same Day"])
payment_type = st.selectbox("Type (Payment Type)", ["Debit", "Credit Card", "Cash", "Other"])

qty = st.number_input("Order Item Quantity", min_value=1, value=1)
discount = st.number_input("Order Item Discount", min_value=0.0, value=0.0)
profit_ratio = st.number_input("Order Item Profit Ratio", value=0.10)
sales = st.number_input("Sales", min_value=0.0, value=100.0)

days_for_shipment = st.number_input("Days for shipment (scheduled)", min_value=1, value=3)

# Auto calculate required engineered fields
order_date_dt = datetime.combine(order_date, datetime.min.time())
order_hour = 12  # middle of the day since no time is given
order_day_of_week = order_date_dt.weekday()
order_month = order_date_dt.month
order_quarter = (order_date_dt.month - 1) // 3 + 1
order_day_of_month = order_date_dt.day
is_weekend = 1 if order_day_of_week >= 5 else 0
is_business_hours = 1  # assume business order
is_month_end = 1 if order_day_of_month >= 25 else 0
urgent_shipment = 1 if days_for_shipment <= 2 else 0

discount_per_item = discount / (qty + 1)
price_per_item = sales / (qty + 1)
high_discount_flag = 1 if discount > discount * 0.75 else 0

# Create dataframe
input_data = pd.DataFrame([{
    "Days for shipment (scheduled)": days_for_shipment,
    "order_hour": order_hour,
    "order_day_of_week": order_day_of_week,
    "order_month": order_month,
    "order_quarter": order_quarter,
    "order_day_of_month": order_day_of_month,
    "is_weekend": is_weekend,
    "is_business_hours": is_business_hours,
    "is_month_end": is_month_end,
    "Shipping Mode": shipping_mode,
    "Type": payment_type,
    "Department Id": 1,
    "Category Id": 1,
    "Product Category Id": 1,
    "Order Item Quantity": qty,
    "Order Item Discount": discount,
    "Order Item Profit Ratio": profit_ratio,
    "Sales": sales,
    "Order Item Total": sales,
    "discount_per_item": discount_per_item,
    "high_discount_flag": high_discount_flag,
    "price_per_item": price_per_item,
    "urgent_shipment": urgent_shipment
}])

# ------------------------------------------------
# PREDICT BUTTON
# ------------------------------------------------
if st.button("Predict Late Delivery Risk"):
    try:
        pred = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]

        if pred == 1:
            st.error(f"⚠️ High Risk of Late Delivery (Probability: {prob:.2f})")
        else:
            st.success(f"🟢 Delivery Likely On Time (Probability: {prob:.2f})")
    except Exception as e:
        st.error(f"Error: {e}")

st.info("Model used: " + metadata["best_model"])
