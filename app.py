import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Load the trained XGBoost model
model = joblib.load('churn_prediction_model.pkl')

# Create a Streamlit web app
st.title('Churn Prediction App')

st.write('Enter customer information to predict churn:')
customer_id = st.text_input('Customer ID')
name = st.text_input('Name')
age = st.number_input('Age')
gender = st.selectbox('Gender', ['Male', 'Female'])
location_mapping = {
    'Chicago': 0,
    'Houston': 1,
    'Los Angeles': 2,
    'Miami': 3,
    'New York': 4
}
location = st.selectbox('Location', list(location_mapping.keys()))
subscription_length_months = st.number_input('Subscription Length (in months)')
monthly_bill = st.number_input('Monthly Bill')
total_usage_gb = st.number_input('Total Usage (in GB)')

# Create a DataFrame with user input, excluding 'CustomerID' and 'Name'
user_data = pd.DataFrame({
    'Age': [age],
    'Gender': [1 if gender == 'Male' else 0],
    'Location': [location_mapping[location]],
    'Subscription_Length_Months': [subscription_length_months],
    'Monthly_Bill': [monthly_bill],
    'Total_Usage_GB': [total_usage_gb]
})

# Preprocess the input data to match the format used during training
# This may include encoding categorical variables, scaling, and feature engineering
def preprocess_input(input_data):
    # Feature engineering
    input_data['Total_Cost'] = input_data['Monthly_Bill'] * input_data['Subscription_Length_Months']
    input_data['Monthly_Usage_per_Subscription'] = input_data['Total_Usage_GB'] / input_data['Subscription_Length_Months']

    # Standard scaling
    sc = StandardScaler()
    input_data[['Monthly_Bill', 'Total_Usage_GB', 'Subscription_Length_Months', 'Total_Cost', 'Monthly_Usage_per_Subscription']] = sc.fit_transform(input_data[['Monthly_Bill', 'Total_Usage_GB', 'Subscription_Length_Months', 'Total_Cost', 'Monthly_Usage_per_Subscription']])

    return input_data


if st.button('Predict Churn'):
    # Preprocess the input data
    preprocessed_data = preprocess_input(user_data)

    # Make predictions using the loaded model
    prediction = model.predict(preprocessed_data)

    if prediction[0] == 0:
        st.write('Churn Prediction: Not Churned')
    else:
        st.write('Churn Prediction: Churned')