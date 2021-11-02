# Accident level predictor
Classify the Accident level using Description

## Data Cleaning
Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. When combining multiple data sources, there are many opportunities for data to be duplicated or mislabeled. 
In this project, we just split the data into two types train data and test data to avoid data leakage for new data and remove the word punctuations and Renaming column names for easy access and converting to unique word and performed vectorization.

## Modeling

Model Training based on trial and error method or by experience, we select the algorithm and train with the selected features.After modelling save the model to pickle file for deployment.

## Streamlit Framework
Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.

## Deployement on Heroku
Once the model has good accuracy, we deploy the model either in the cloud.Heroku is a container-based cloud Platform as a Service (PaaS).

## Installation and Run
Install Required Libraries

     Step 1: pip install -r requirements.tx
     
Running Project

     Step 2: Streamlit run app.py