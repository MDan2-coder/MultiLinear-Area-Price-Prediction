import pickle
import streamlit as st
model1=pickle.load(open("PricePredic.pkl","rb"))
def mydeploy():
    st.title("Area Price Prediction")
    area=st.number_input("Enter your area :")
    bedrooms=st.number_input("Enter numbers of bedrooms :")
    age=st.number_input("Enter age of house :")
    pred=st.button("predict")
    if pred:
        x=model1.predict([[area,bedrooms, age]])
        st.write("Area price is ",x[0],"₹")
mydeploy()
