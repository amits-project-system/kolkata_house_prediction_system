import streamlit as st
import pandas as pd
import joblib
model_data = joblib.load('data.pkl')
model = joblib.load('model5.pkl')
st.title("Kolkata House Price Prediction")
st.write("Enter the details of the house to predict its price.")
model_input_data=model_data.drop('Price(cr)', axis=1)
input_data=[]
for column in model_input_data.columns:


    if column == 'Location':
        values=st.selectbox(f"Select your desired location where you buy a bulding ", model_input_data[column].unique())
    elif column == 'House_Type':
        values=st.selectbox(f"Select which type of the house you are looking for", model_input_data[column].unique())
    elif column == 'BHK':
        values=st.selectbox(f"select how many BHK you need", [1,2,3,4,5,6,7])
    elif column == 'Area(sqft)':
        values=(st.slider(f"slide how much area you need for your building:", min_value=0, max_value=2000, step=1))
    elif column == 'Furnishing':
        values=st.selectbox(f"select how furnish you need for your bulding", model_input_data[column].unique())
    input_data.append(values)
new_data=pd.DataFrame([input_data],
                      columns=['Area(sqft)','Furnishing','Location','BHK','House_Type'])
st.write(new_data)
st.write(new_data.dtypes)

if st.button('Predict'):
    prediction = model.predict(new_data)
    st.success(f"The predicted price of the house is: RS.{(prediction[0]*10000000).astype(int):,} ")