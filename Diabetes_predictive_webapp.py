# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 22:01:54 2023

@author: subit
"""

import numpy as np
import pickle
import streamlit as st

# Loading the saved model
loaded_model = pickle.load(open(r"C:\Users\subit\trainedModel.sav",'rb'))

# Creating a function for Prediction
def diabetes_predictive_system(input_data):
    # input_data = (1,85,66,29,0,26.6,0.351,31)
    # input_data = (6,148,72,35,0,33.6,0.627,50)
    # traform list to numpy array
    input_data_array = np.asarray(input_data)

    # reshape the array
    input_data_reshapped = input_data_array.reshape(1,-1)



    prediction = loaded_model.predict(input_data_reshapped)
    print(prediction)
    if prediction[0] == 0:
        return 'Person does not have diabetes'
    else:
        return 'Person have diabetes'
    
    
def main():
    
    
    # giving the title
    st.title("Diabetes Prediction web app")
    
    # Getting the input data from user
    # All Features except target: Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age
    
    Pregnancies = st.text_input("Number of Pregnancies: ")
    Glucose = st.text_input("Glucose Level: ")
    BloodPressure = st.text_input("Blood Pressure Value: ")
    SkinThickness = st.text_input("Skin Thickness value: ")
    Insulin = st.text_input("Insulin Level: ")
    BMI = st.text_input("BMI value: ")
    DiabetesPedigreeFunction = st.text_input("Diabetes Predigree Function value: ")
    Age = st.text_input("Age of the Person: ")
    
    
    # Code for Prediction
    diagnosis = ''
    
    # Creating a button for prediction
    
    if st.button("Diabetes test result"):
        diagnosis = diabetes_predictive_system([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
        
    st.success(diagnosis)
    
    
    
    
if __name__ == '__main__':
    main()