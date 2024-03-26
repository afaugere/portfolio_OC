# importation des librairies classiques
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
import pytest
# importation pour tests
from fastapi.testclient import TestClient
from fastapi import status 
from main import app
# instanciation variable
client=TestClient(app=app)
# test de bon démarrage
def test_read():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the AF ML Model API"}
# test du retour SOLVABLE client sur client index 3
def test_classifier():
    response = client.post('/predict', json = {'ID_CLIENT' : 3})
    assert response.json() == {'label' : [0], 'probability' : [0.030205467881345805]}
