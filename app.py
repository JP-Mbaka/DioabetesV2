"""
 @author: Mbaka JohnPaul

 """

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from darb import Darb
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib 

app = FastAPI()

# Load Model
model = joblib.load("rfcModel.pkl")

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["*"] for all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/predict')
def predict_diabetes(data:Darb):
    data = data.dict()
    preg = data['preg']
    plas = data['plas']
    pres = data['pres']
    skin = data['skin']
    insu = data['insu']
    mass = data['mass']
    pedi = data['pedi']
    age = data['age']

    prediction = model.predict([[preg, plas, pres, skin, insu, mass, pedi, age]])

    # rfc.predict([[2,3,4,5,45.2,2.1,35,6]])
    return{
        'prediction': prediction[0]
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port= 8000)
else:
    uvicorn.run(app, host="0.0.0.0", port=8000)
