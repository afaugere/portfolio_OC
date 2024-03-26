import numpy as np
import pandas as pd
import streamlit as st
import json
import requests

st.image("https://capirossi.org/wp/wp-content/uploads/2019/04/Fonction-finance-salaires-globalement-hausse-2019-F1-1100x4801.jpg")
st.title("Scoring_Model_AFAUGERE")
st.header("Mise en place d'un modèle de scoring pour évaluer la solvabilité Client")
st.info("Basé sur un échantillon de 200 clients allant de 0 à 199, le seuil de décision est à 0.7")
st.markdown("___")
st.markdown(
    """
    ### Objectifs
    ##### Determiner la solvabilité Client (Solvable/Non Solvable)
    ##### Situer le Client vis à vis du seuil de décision et des autres Clients
    ##### Situer le Client sur les critères qui ont abouti à la décision
    """
)
st.markdown("___")

st.sidebar.write("")
st.sidebar.write("select index of client bellow")
client = st.sidebar.slider("Index Client", 0, 199, 1)

# conversion des données d'entrée en json
input = {"ID_CLIENT" : client}


if st.sidebar.button("predict") :
    res1 = requests.post(url = "https://apiafgha.onrender.com/predict", data = json.dumps(input))
    res2 = requests.post(url = "https://apiafgha.onrender.com/interpretation", data = json.dumps(input))
    st.subheader(res1.text)
    st.subheader(res2.text)





