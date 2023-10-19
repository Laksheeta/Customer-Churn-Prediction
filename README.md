# Churn Prediction Project

This project focuses on predicting customer churn using machine learning techniques. Customer churn, or customer attrition, occurs when customers stop doing business with a company. Predicting and preventing churn is crucial for businesses as it helps retain customers and reduce revenue loss.

## Table of Contents
- [Dataset](#dataset)
- [1. Data Preprocessing](#1-data-preprocessing)
- [2. Feature Engineering](#2-feature-engineering)
- [3. Model Building](#3-model-building)
- [4. Model Optimization](#4-model-optimization)
- [5. Model Deployment](#5-model-deployment)
- [For Model Deployment](#For-Model-Deployment)

## Dataset

The dataset used in this project contains the following columns:
- CustomerID
- Name
- Age
- Gender
- Location
- Subscription_Length_Months
- Monthly_Bill
- Total_Usage_GB
- Churn (the target variable)

## 1. Data Preprocessing

In the data preprocessing stage, we perform the following tasks:
- Load the dataset and perform initial data exploration.
- Handle missing data and outliers.
- Prepare the data for machine learning by encoding categorical variables and splitting it into training and testing sets.

## 2. Feature Engineering

To improve the model's prediction accuracy, we generate relevant features from the dataset. Feature engineering involves:
- Creating new features, such as 'Total_Cost' and 'Monthly_Usage_per_Subscription.'
- Applying feature scaling or normalization when necessary.

## 3. Model Building

In the model-building stage, we choose appropriate machine learning algorithms and train and validate the selected model on the training dataset. Evaluation metrics such as accuracy, precision, recall, and F1-score are used to assess model performance.

## 4. Model Optimization

To fine-tune the model and improve predictive performance, we explore techniques like cross-validation and hyperparameter tuning. Multiple machine learning algorithms may be compared to identify the best-performing model.

## 5. Model Deployment

Once satisfied with the model's performance, we deploy it in a production-like environment. The model can take new customer data as input and provide churn predictions.

## For Model Deployment
- Go to the comment prompt.
- Go to the file location where app.py file is located
- Run the following code: "streamlit run app.py"
