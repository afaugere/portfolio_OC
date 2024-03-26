# importation des librairies
from fastapi import FastAPI
import uvicorn
import numpy as np
import pandas as pd
import shap
from joblib import load
import os
from lightgbm import LGBMClassifier
import json
from pydantic import BaseModel, json
import sklearn

# instanciation des objets
app = FastAPI()
# importation du modèle
model = load('model_LGBMC_best.joblib')

# importation data
df = pd.read_csv("df_test_norm.csv")
df = df[0:200]

@app.get("/")
def read_root():
    return {"message": "Welcome to the AF ML Model API"}
# Définition des requêtes
class Request_body(BaseModel):
    ID_CLIENT: int
# Enpoint prediction probabilité

@app.post('/predict')
# fonction de prédiction
def predict_labels(input_data : Request_body) :
# nouvelles données
    input_data = input_data.dict()
# prédiction
    client =  df.loc[input_data["ID_CLIENT"]].values
    client = np.reshape(client, (1,-1))
    prediction_proba = model.predict_proba(client)
# definition du seuil
    seuil = 0.07
# colonne avec prediction 1
    prediction_proba_one = prediction_proba[:,1]
# colonne avec seuil
    predict_proba_label = (prediction_proba_one > seuil).astype(int)
    # return f" label : {predict_proba_label}, probability : {prediction_proba_one}" 
    return {'label' : predict_proba_label.tolist(), 'probability' : prediction_proba_one.tolist()} 

# Endpoint interprétabilité
@app.post('/interpretation')
# Fonction interprétation locale
def interpretation(input_data : Request_body) :
    input_data = input_data.dict()
#  Interprétation
    client =  df.loc[input_data["ID_CLIENT"]].values
    client = np.reshape(client, (1,-1))
    explainer = shap.TreeExplainer(model[1])
    shap_values = explainer.shap_values(client)
    df_shap_values = pd.DataFrame(shap_values[1], columns = df.columns)
    return df_shap_values






