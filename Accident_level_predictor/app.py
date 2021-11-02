import streamlit as st
import pickle
import string
import base64
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
#Pickle files
tf_idf = pickle.load(open('tfvect.pkl','rb'))
model = pickle.load(open('model_PA.pkl','rb'))
st.markdown("<h1 style='text-align: center; color: black;'>Industrial Safety and health database</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Accident Level Predictor</h3>", unsafe_allow_html=True)
input_text = st.text_area("Enter Your Description Here 📰")
if st.button('Predict'):
    # 1. preprocess
    transformed_text= input_text
    # 2. vectorize
    vector_input = tf_idf.transform([transformed_text])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 'I':
        st.header('Level-1')
    elif result == 'II':
        st.header("Level-2")
    elif result == 'III':
        st.header("Level-3")
    elif result == 'IV':
        st.header("Level-4")
    else:
        st.header("Level-5")