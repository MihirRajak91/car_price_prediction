import numpy as np
import pandas as pd
import streamlit as st
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

st.title('Predicting Price Of Used Cars')
st.write("---")
st.text('the data obtained from Kggle was cleaned and preprocessed')
st.text('In this Project, we are going to predict the Price of Used Cars using various features like Present_Price, Selling_Price, Kms_Driven, Fuel_Type, Year etc. The data used in this project was downloaded from Kaggle.')
st.markdown("DataSet of reviews of Amazon products obatined from Kaggle")
df = pd.read_csv('car_price_data2.csv')
df2 = pd.read_csv('car_price_data2_Final.csv')
#-------------------------------------------------------model creation

# Training model
#st.text('Linear Regression')
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
df
st.write("---")

st.subheader('Car price prediction')

st.write("---")
#-----------------------------------------------------model creation end
with st.form(key='my_form'):
    Present_Price = st.text_input('Present_Price')
    Car_age= st.text_input('Car_age')
    Fuel_Type_Diesel = st.text_input('Fuel_Type_Diesel')
    Seller_Type_Individual= st.text_input('Seller_Type_Individual')
    Transmission_Manual = st.text_input('Transmission_Manual')
    submit_button = st.form_submit_button('Predict')
try:
    
    r_data = {'Selling_Price':["Selling_Price"],'Present_Price':["Present_Price"], 'Car_age':["Car_age"], 'Fuel_Type_Diesel':["Fuel_Type_Diesel"], 'Seller_Type_Individual':["Seller_Type_Individual"],'Transmission_Manual':["Transmission_Manual"]}
    review_data_df = pd.DataFrame(r_data)
    X = review_data_df.drop('Selling_Price', axis=1)
    review_review_cat = lr.predict(X)
    st.write("---")
    st.write(review_review_cat)

except:
    print("error")




