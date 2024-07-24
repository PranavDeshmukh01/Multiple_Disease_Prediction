# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:51:12 2024

@author: pranav
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open('C:/Users/prana/Desktop/Multiple_Disease_Prediction/Saved Models/diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('C:/Users/prana/Desktop/Multiple_Disease_Prediction/Saved Models/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('C:/Users/prana/Desktop/Multiple_Disease_Prediction/Saved Models/parkinsons_model.sav','rb'))

#sidebar for navigate

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                           default_index=0)
#Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    #page title
    st.title('Diabetes Prediction using ML')  

if (selected == "Heart Disease Prediction"):

    #page title
    st.title('Heart Disease Prediction using ML')

if(selected == 'Parkinsons Prediction'):
    #page title
    st.title('Parkinsons Prediction using ML')
    