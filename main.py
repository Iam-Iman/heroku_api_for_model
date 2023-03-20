# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 07:42:14 2023

@author: Iman Ngwepe
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class model_input(BaseModel):
    
    age : int
    sex : int 
    cp : int  
    trestbps : int 
    chol : int  
    fbs : int  
    restecg : int  
    thalach : int  
    exang : int  
    oldpeak : float
    slope : int  
    ca : int 
    thal : int

# load saved model
heart_model = pickle.load(open('heart_model.sav', 'rb'))

#create API
@app.post('/heart_disease_prediction')
def heart_pred(input_parameters : model_input):
    # convert json to dict
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    # convert dict to list(keys)
    age = input_dictionary['age']
    gender = input_dictionary['sex']
    cp_type = input_dictionary['cp']
    resting_bp = input_dictionary['trestbps']
    cholesterol = input_dictionary['chol']
    fasting_bs = input_dictionary['fbs']
    resting_ecg = input_dictionary['restecg']
    max_heart_rate = input_dictionary['thalach']
    exercise_angina = input_dictionary['exang']
    exercise_depression = input_dictionary['oldpeak']
    peak_exercise = input_dictionary['slope']
    major_vessels = input_dictionary['ca']
    failure_type = input_dictionary['thal']
    
    input_list = [age, gender, cp_type, resting_bp, cholesterol, fasting_bs,
                  resting_ecg, max_heart_rate, exercise_angina, exercise_depression,
                  peak_exercise, major_vessels, failure_type ]
    
    prediction = heart_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'Patient does not have heart disease'
    else:
        return 'Pateient has heart problems'
    
