import numpy as np
import pandas as pd
import streamlit as st
import json
import requests
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def main() :
    # liens vers application
    
    URL_PRED = "https://apiafgha.onrender.com/predict"
    URL_IMPORTANCE = "https://apiafgha.onrender.com/interpretation"
    
    # Accueil
    st.image("https://capirossi.org/wp/wp-content/uploads/2019/04/Fonction-finance-salaires-globalement-hausse-2019-F1-1100x4801.jpg")
    st.title("Evaluation Solvabilité Client")
    st.header("Analyse des résultats du modèle de scoring")
    st.info("Basé sur un échantillon de 200 clients allant de 0 à 199, le seuil de décision est à 7")
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
    # Chargement des données
    lst_client = np.arange(0,200,1)
    @st.cache_data(persist =True)
    def load_proba_label_importance(lst_client):
        lst_proba = []
        lst_label = []
        dico_feature_importance = {}
        for nb in lst_client :
            clt_id = int(nb)
            input = {'ID_CLIENT' : clt_id}
            res_pred_all = requests.post(url = URL_PRED, data = json.dumps(input))
            res_f_imp_all = requests.post(url = URL_IMPORTANCE, data = json.dumps(input))
            lst_proba.append(res_pred_all.json()["probability"])
            lst_label.append(res_pred_all.json()["label"])
            dico_feature_importance[clt_id] = res_f_imp_all.json()
        # création dataframe avec toutes proba et changement d'echelle
        df_prob = pd.DataFrame(lst_proba, columns = ["proba"])*100
        df_prob["label"] = lst_label
        df_prob["label"] = df_prob["label"].apply(lambda x : "refusé" if x == [1] else "accepté")
        # transformation du dico_feature_importance en dataframe
        df_importance = pd.DataFrame.from_dict(dico_feature_importance, orient = 'index')
        for col in df_importance.columns :
            df_importance[col]=df_importance[col].apply(lambda x : x['0'])
        df = df_prob.merge(df_importance, left_index=True, right_index = True)
        return(df)
    df = load_proba_label_importance(lst_client)
    # définition des features
    features = df.columns[2:].to_list()
    # définition des quartiles et moyenne
    Q1 = float(df["proba"].quantile(0.25))
    Q2 = float(df["proba"].quantile(0.50))
    Q3 = float(df["proba"].quantile(0.75))
    Q4 = float(df["proba"].quantile(1))
    mean = float(df["proba"].mean())
    # widgjet
    st.sidebar.write("")
    st.sidebar.markdown("""
        ### **Mode d'emploi** :
        #### *1) Choisir l'index client avec la sidebar*
        #### *2) Choisir un critère (feature) pour l'analyser avec la position du Client*
        #### *3) Choisir les axes pour analyser le comportement global des critères(features)*                
        """)
    st.sidebar.write("## select index of client bellow :dart:")
    client = st.sidebar.slider("#### Index Client", 0, 199, 1)
    st.sidebar.write("")
    st.sidebar.write("## select feature bellow :microscope:")
    feature = st.sidebar.selectbox('#### select',features)
    # assignation selectbox pour feature importance
    selected_feature = feature
    st.sidebar.write("")
    st.sidebar.write("## select Axes bellow :chart_with_upwards_trend:")
    feature_x = st.sidebar.selectbox('#### select axe X',features)
    feature_y = st.sidebar.selectbox('#### select axe Y',features)
    score = df["proba"][client]
    if score < 7 : 
        st.sidebar.markdown("## Résultat : accepté :white_check_mark:")
    else : 
        st.sidebar.markdown("## Résultat : refusé :x:")

    # graphuique jauge probabilité
    def jauge_probabilité(client) :
        fig = go.Figure(go.Indicator(
                mode = "gauge+number+delta",
                value = df["proba"][client],
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "position du client selon le seuil de décision"},
                delta = {'reference': 7, 'decreasing': {'color': "green"}, 'increasing' : {'color' : 'red'}},
                gauge = {
                    'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                    'bar': {'color': "darkblue"},
                    'bgcolor': "white",
                    'borderwidth': 2,
                    'bordercolor': "gray",
                    'steps': [
                        {'range': [0, 7], 'color': 'green'},
                        {'range': [7, 100], 'color': 'red'}],
                    'threshold': {
                        'line': {'color': "yellow", 'width': 4},
                        'thickness': 1,
                        'value': 7}}))
        fig.update_layout(font = {'color': "darkblue", 'family': "Arial"})
        st.plotly_chart(fig)
    score = df["proba"][client]
    if score < 7 : 
        st.write("### Résultat : accepté :white_check_mark:")
    else : 
        st.write("### Résultat : refusé :x:")
    st.write("#### Jauge de score client avec seuil de décision :")
    st.write(f"Seuil : 7")
    st.write(f"Score Client : {score.round(3)}")
    jauge_probabilité(client)
    st.markdown("___")

    # graphuique moyenne
    def jauge_moyenne(client) :
            fig2 = go.Figure(go.Indicator(
                mode = "gauge+number+delta",
                value = df["proba"][client],
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "position du client selon Moyenne"},
                delta = {'reference': mean, 'decreasing': {'color': "green"}, 'increasing' : {'color' : 'red'}},
                gauge = {
                    'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                    'bar': {'color': "darkblue"},
                    'bgcolor': "white",
                    'borderwidth': 2,
                    'bordercolor': "gray",
                    'steps': [
                        {'range': [0, mean], 'color': 'green'},
                        {'range': [mean, 100], 'color': 'red'}],
                    'threshold': {
                        'line': {'color': "yellow", 'width': 4},
                        'thickness': 1,
                        'value': mean}}))
            fig2.update_layout(font = {'color': "darkblue", 'family': "Arial"})
            st.plotly_chart(fig2)
    st.write("#### Jauge de score client avec Moyenne :")
    st.write(f"Moyenne : {mean}")
    st.write(f"Score Client : {score.round(3)}")
    jauge_moyenne(client)
    st.markdown("___")

    # graphuique Mediane
    def jauge_mediane(client) :
            fig3 = go.Figure(go.Indicator(
                mode = "gauge+number+delta",
                value = df["proba"][client],
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "position du client selon Mediane"},
                delta = {'reference': Q2, 'decreasing': {'color': "green"}, 'increasing' : {'color' : 'red'}},
                gauge = {
                    'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                    'bar': {'color': "darkblue"},
                    'bgcolor': "white",
                    'borderwidth': 2,
                    'bordercolor': "gray",
                    'steps': [
                        {'range': [0, Q1], 'color': 'blue'},
                        {'range': [Q1, Q2], 'color': 'green'},
                        {'range': [Q2, Q3], 'color': 'orange'},
                        {'range': [Q3, Q4], 'color': 'red'}],
                    'threshold': {
                        'line': {'color': "yellow", 'width': 4},
                        'thickness': 1,
                        'value': Q2}}))
            fig3.update_layout(font = {'color': "darkblue", 'family': "Arial"})
            st.plotly_chart(fig3)
    st.write("#### Jauge de score client avec Mediane :")
    st.write(f"Mediane : {Q2}")
    st.write(f"Score Client : {score.round(3)}")
    jauge_mediane(client)
    st.markdown("___")       

    # graphuique interprétation locale et globale
    feature_importance_globale = df[features].mean()
    def interpret_loc_glob(client) :
            # Creating two subplots
            fig7 = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                                shared_yaxes=True, vertical_spacing=0.001)

            fig7.append_trace(go.Bar(
                x=df[features].loc[client],
                y=df[features].columns.to_list(),
                marker=dict(
                    color='rgba(50, 171, 96, 0.6)',
                    line=dict(
                        color='rgba(50, 171, 96, 1.0)',
                        width=1),
                ),
                name='Ferature importance locale',
                orientation='h',
            ), 1, 1)

            fig7.append_trace(go.Scatter(
                x=feature_importance_globale, 
                y=df[features].columns.to_list(),
                mode='lines+markers',
                line_color='rgb(128, 0, 128)',
                name='Ferature importance globale',
            ), 1, 2)

            fig7.update_layout(
                title='Comparaison feature importance locale et globale',
                yaxis=dict(
                    showgrid=True,
                    showline=True,
                    showticklabels=True,
                    domain=[0, 0.85],
                ),
                yaxis2=dict(
                    showgrid=True,
                    showline=True,
                    showticklabels=False,
                    linecolor='rgba(102, 102, 102, 0.8)',
                    linewidth=2,
                    domain=[0, 0.85],
                ),
                xaxis=dict(
                    zeroline=True,
                    showline=False,
                    showticklabels=True,
                    showgrid=True,
                    domain=[0, 0.5],
                ),
                xaxis2=dict(
                    zeroline=True,
                    showline=False,
                    showticklabels=True,
                    showgrid=True,
                    domain=[0.5, 1],
                    dtick=25000,
                ),
            legend=dict(x=0.029, y=1.038, font_size=10),
            margin=dict(l=100, r=20, t=70, b=70),
            )

            fig7.update_layout(xaxis_title = "Importance locale",
                            xaxis2_title = "Importance globale",
                            height = 800, 
                            width=800)

            fig7.update_yaxes(automargin=True)
            st.plotly_chart(fig7)
    st.write("#### Comparaison feature importance globale et locale :")
    interpret_loc_glob(client)
    st.markdown("___")
    
    
    def interpret_client(client) :
            # Features importance
            # values
            x = df[features].loc[client]
            y = df[features].columns.to_list()
            # color_list
            zero = 0
            colors=['blue' if val < zero else 'red' for val in x]

            fig4 = go.Figure(go.Bar(
                x = x,
                y = y,
                marker= {'color': colors},
                orientation='h'))

            fig4.update_layout(title="Importance des features dans la décision",
                            xaxis_title = "Importance",
                            font = dict(size =8), 
                            height = 600, 
                            width=1000)
            fig4.update_yaxes(automargin=True)
            st.plotly_chart(fig4)
    st.write("#### Evaluation de l'importance des critères dans la notation du Client :")
    interpret_client(client)
    st.markdown("___") 
    
    # graphuique feature importance focus all client
    def graph_feature_selected(client, selected_feature) :
            # confirmation de la colone label en str
            df["label"] = df["label"].astype(str)
            df_feature_selected = df[['label',selected_feature]]
            # histogramme
            fig5 = px.histogram(df_feature_selected, x=selected_feature, color="label",  marginal="rug",
                            color_discrete_map={"refusé" : "red", "accepté" : "green"},
                            hover_data=df_feature_selected.columns, barmode="overlay")
            # ajout du point client
            fig5.add_trace(go.Scatter(x=[df_feature_selected[selected_feature][client]], 
                                    y = [0],
                                    name='Client',
                                    marker = dict(color='blue',
                                                symbol = "cross",
                                                size=10),
                                    mode='markers'))
            # ajout de la ligne client
            fig5.add_vline(x= df_feature_selected[selected_feature][client], 
                        line_width=1, 
                        line_dash="dash", 
                        line_color="blue")

            fig5.update_traces(opacity=0.9) 
            
            fig5.update_layout(title=f"Importance feature {selected_feature} clients",
                        xaxis_title = f"{selected_feature}")
            st.plotly_chart(fig5)
    st.write("#### Position du client vs autres clients sur critère selectionné :")
    graph_feature_selected(client, selected_feature)
    st.markdown("___") 

    def graph_f_similar_client(selected_feature, client) :
            df_feature_selected = df[['label','proba',selected_feature]]
            lim_basse = 5
            lim_haute = 5
            df_feature_selected_sim = df_feature_selected[(df_feature_selected["proba"]<df_feature_selected["proba"].loc[client]+lim_haute)&(df_feature_selected["proba"]>df_feature_selected["proba"].loc[client]-lim_basse)]
            color_map = {'refusé':'red', 'accepté':'green'}
            label_color =  df_feature_selected_sim['label'].map(color_map)
            
            fig6 = px.histogram(df_feature_selected_sim, x=selected_feature, color="label",  marginal="rug",
                            color_discrete_map={"refusé" : "red", "accepté" : "green"},
                            hover_data=df_feature_selected.columns, barmode="overlay")

            fig6.add_trace(go.Scatter(x=[df_feature_selected_sim[selected_feature][client]], 
                                    y = [0],
                                    name='Client',
                                    marker =dict(color='blue',
                                                symbol = "cross",
                                                size=10),
                                    mode='markers'))

            fig6.add_vline(x= df_feature_selected_sim[selected_feature][client], 
                        line_width=1, 
                        line_dash="dash", 
                        line_color="blue")
            
            fig6.update_traces(opacity=0.9)
            
            fig6.update_layout(title=f"Importance feature {selected_feature} clients similaires",
                        xaxis_title = f"{selected_feature}")

            st.plotly_chart(fig6)
    st.write("#### Position du client vs clients similaires sur critère selectionné :")
    graph_f_similar_client(selected_feature, client)
    st.markdown("___") 

    def analyse_both_feature(feature_x, feature_y):
        fig8 = px.scatter(df, x= feature_x, y= feature_y, trendline="ols", color_discrete_sequence=['blue'])
        fig8.update_layout(title = f"Analyse bivarié feature importance",
                            height = 800, 
                            width=800) 
        st.plotly_chart(fig8)
    st.write("#### Analyse globale entres les features :")
    analyse_both_feature(feature_x, feature_y)
    st.markdown("___") 

if __name__ == '__main__':
    main()






