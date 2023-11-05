# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 11:59:40 2023

@author: vidya chavan
"""

import streamlit as st
import numpy as np
import pandas as pd
import pickle

pickle_in = open("C:\\Users\\hp\\OneDrive\\Desktop\\p285\\regressor_r .pkl",'rb' )
regressor_r = pickle.load(pickle_in)

def predict_energy_production(temperature,exhaust_vacuum,amb_pressure,r_humidity):


    prediction = regressor_r.predict([[temperature,exhaust_vacuum,amb_pressure,r_humidity]])
    print(prediction)
    return prediction

def main():
    
    st.title('Combined-Cycle Power Plant Energy Prediction')
    html_temp = """
    #<div style = 'background-color:teal;padding:10px'>
    #<h2  style = 'color:white;text-align:center;'>Energy Predictor App </h2>
    #</div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    temperature = st.text_input("temperature","Type Here")
    exhaust_vacuum	= st.text_input("exhaust_vacuum","Type Here")
    amb_pressure = st.text_input("amb_pressure","Type Here")
    r_humidity = st.text_input("r_humidity","Type Here")
    result = ""
    if st.button("Predict"):
        result = predict_energy_production(temperature,exhaust_vacuum,amb_pressure,r_humidity)
    st.success('The output is{}'. format(result))


if __name__ == '__main__':
    main()