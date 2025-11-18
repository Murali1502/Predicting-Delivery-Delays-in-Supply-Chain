# Late Delivery Risk Prediction

Dataset used: 
https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis/data

PowerBI Dashboard:
https://github.com/PolinaBurova/Supply-Chain-Performance-Dashboard

## Summary

- This project aimed to predict the risk of late deliveries in a supply chain dataset using machine learning models. We applied Logistic Regression, Random Forest, and XGBoost, achieving consistent and high model performance, with accuracies around **97.4%** across all models.
- It was assumed that accurately predicting late delivery risk rather than no-risk was of highest importance to the business. Therefore, the predictive model was optimized for sensitivity (recall). 
- The main focus was to identify key features driving the risk of late delivery, such as shipment timing, payment method, and the variance between scheduled and actual shipping days. The project successfully highlighted how machine learning can help manage supply chain performance and mitigate operational risks.

## Approach

### 1. Exploratory Data Analysis (EDA)
- Conducted an in-depth analysis of the dataset.
- Key insights were drawn regarding delivery delays, including a visualization that showed the **variance in delivery dates** across different shipping modes:
![Delivery Date Variance](https://github.com/PolinaBurova/Predicting-Delivery-Delays-in-Supply-Chain/blob/main/DeliveryDate_Risk.png)
*This chart visualized the variance in shipping days, clearly showing which shipping methods had the highest inconsistency in delivery performance(First and Second Classes).*


### 2. Feature Selection
- **Chi-square test** for categorical variables such as payment methods and shipping modes.
- **Variance threshold** to remove low-variance features.
- **Correlation analysis** to handle multicollinearity between features.
- Applied **Recursive Feature Elimination (RFE)** with Logistic Regression, selecting the top 15 most relevant features to be used out of an initial set of 27.

### 3. Data Preprocessing
- Handled **missing values** and **outliers** effectively.
- Scaled and encoded features, and checked for any class imbalances to ensure a robust model.

### 4. Model Optimization
- **Hyperparameter tuning** using GridSearchCV was performed to fine-tune models and avoid overfitting.
- Emphasized **recall** as the key metric to minimize false negatives.
- **Feature importance** and **coefficients** were analyzed, revealing the most influential features for predicting late deliveries:

![LR Feature Coefficients](https://github.com/PolinaBurova/Predicting-Delivery-Delays-in-Supply-Chain/blob/main/Features_Ranking1.png)

![RF and XGBoost Ranking](https://github.com/PolinaBurova/Predicting-Delivery-Delays-in-Supply-Chain/blob/main/Features_Ranking2.png)

## Results
- The models evaluated (Logistic Regression, Random Forest, and XGBoost) all performed exceptionally well, achieving **97.4% accuracy** and a recall of 1.
- The key features identified as critical in predicting late delivery risk were **Days for shipping (real)**, which showed a positive correlation—indicating longer actual shipping times increased the risk of late delivery—and **Days for shipment (scheduled)**, which had a negative correlation, suggesting better planning reduces delays. 
- **Shipping Mode** also significantly impacted risk, with Same Day delivery reducing risk due to faster, more optimized logistics, while First Class posed the highest risk due to longer fulfillment times and logistical inconsistencies. The **Order_to_Shipment_Time**, representing fulfillment time, highlighted how reducing the time from order placement to shipment improved delivery performance. 
- Lastly, **Payment methods**, particularly Transfer, were found to be a key predictor of late deliveries, adding another dimension to optimizing supply chain efficiency.

By accurately predicting late deliveries, the project demonstrated how machine learning can help optimize supply chain performance, enabling the business to proactively manage risk and ensure timely deliveries. The ability to accurately identify factors like shipping time, payment methods, and operational delays, which directly impact late delivery, provides valuable insights that can help mitigate risks and improve customer satisfaction.

## Improvements
Potential improvements for this project:
- **Advanced feature engineering**: Introduce new features that capture more intricate business-related details.
- **Customer-level analysis**: Looking into customer-specific factors (e.g., geographical regions, customer profiles) could offer additional predictive insights.
- **Real-time integration**: Implement the model in a live system to predict and flag late deliveries before they occur.
