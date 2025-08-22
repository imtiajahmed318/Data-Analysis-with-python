# 💻 Laptop Price Prediction

This project aims to predict the **price of laptops** based on their specifications using supervised machine learning techniques. The dataset contains various features such as processor, RAM, storage, brand, operating system, and more.

## 📁 Dataset

- **Source**: Uploaded via Coders Lab
- **Format**: CSV
- **Target Variable**: `Price`
- **Features Include**:
  - Company (Brand)
  - TypeName
  - RAM
  - Weight
  - Touchscreen
  - IPS
  - Screen Size & Resolution
  - CPU
  - HDD, SSD
  - GPU
  - OS

## 🔍 Exploratory Data Analysis (EDA)

- Checked for missing and duplicated values
- Analyzed correlations between numerical features
- Visualized distributions using histograms, boxplots, and scatter plots
- Examined categorical features like brand and OS

## 🧹 Data Preprocessing

- Converted `Yes/No` features (like Touchscreen, IPS) to binary
- Extracted CPU brand from model strings
- Converted screen size from inches to float
- Extracted resolution and computed PPI (pixels per inch)
- Transformed categorical variables using label encoding / one-hot encoding

## 📊 Modeling

- **Train-test split** (e.g. 80-20)
- Applied regression models like:
  - Linear Regression
  - Ridge/Lasso Regression
  - Random Forest Regressor
  - XGBoost

- **Evaluation Metrics**:
  - R² Score
  - RMSE (Root Mean Squared Error)




## 🧠 Requirements

Install necessary packages with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost
```
