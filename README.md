# Présentation des projets professionnels réalisés

# 0) SOMMAIRE
- I) Systèmes éducatifs
- II) Santé publique
- III) Consommations bâtiments
- IV) Segmentation clients e commerce
- V) Classification des biens de consommation
- VI) Modèle de scoring
- VII) Dashboard
- VIII) Traitement AWS



# I) Systèmes éducatifs

## I.1) Contexte  
- Projet d’extension à l’international d’ ACADEMY qui propose des contenus de formation en ligne pour un public de niveau Lycée et Université

## I.2) But
- Déterminer si les données sur l’éducation de la banque mondiale peuvent informer le projet

## I.3) Objectifs
- Réaliser une analyse pré-exploratoire du jeu de donnée sur la banque mondiale
- Valider la qualité du jeu de données
- Décrire les informations contenues dans le jeu de données
- Sélectionner les informations pertinentes
- Déterminer des ordres de grandeur des indicateurs

## I.4) Le jeu de données
- Statistiques sur l’éduction https://datacatalog.worldbank.org/search/dataset/0038480
- Base de données annuelle (enquêtes, sondages…) : 22/01/23
- Plus de 4000 indicateurs (accès éduction, enseignement, population dépenses…)
- Couverture de plusieurs années jusque 1970 – 2050
- 5 fichiers de données en format csv

## I.5) Librairies
Jupyter Notebook, Python, Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn



# II) Santé publique

## II.1) Contexte  
- Projet d’ amélioration de la base de données Open Food Facts.
- Pour rajouter un produit, il y a de nombreux champs textuels et numériques à remplir, ce qui peut conduire à des erreurs de saisie et à des valeurs manquantes.

## II.2) But
- Créer un système de suggestion ou d’auto-complétion pour aider les usagers à remplir plus
efficacement la base de données

## II.3) Objectifs
- Traiter le jeu de donnée pour le rendre exploitable
- Explorer les données
- Réaliser des tests statistiques pour valider les résultats des analyses
- Rédiger un rapport d’exploration et une conclusion sur la faisabilité du projet
- Respecter les 5 grands principes RGPD

## II.4) Le jeu de données
- Le jeu de données https://fr.openfoodfacts.org
- base de données collaborative de produits alimentaires qui répertorie les ingrédients, les
allergènes, la composition nutritionnelle et toutes les informations présentes sur les étiquettes
des aliments pour aider le consommateur dans ses choix
- Plus de 200 pays, plus de 600000 produits, plus de 9000 contributeurs
- Descriptif des champs du jeu de donnée
- Nutriscore questions réponses https://www.santepubliquefrance.fr

## II.5) Librairies
Jupyter Notebook, Python, Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn, Scipy


# III) Consommations bâtiments

## III.1) Contexte  
- Projet de prédiction des émissions de CO2 et de consommation totale d’énergie des bâtiments non destinés à l’habitation
de la ville de Seattle

## III.2) But
- Créer un système de prédiction des émissions de CO2 et de consommation totale d’énergie des bâtiments non destinés à l’habitation
de la ville de Seattle en se basant sur les données structurelles des bâtiments

## III.3) Objectifs
- Traiter et explorer le jeu de donnée
- Réaliser des modélisations prédictives
- Evaluer les modèles
- Se passer des relevés de consommation annuels et futurs
- Eviter le Data leakage

## III.4) Le jeu de données
- Le jeu de données https://data.seattle.gov/dataset2016-Building-Energy-Benchmarking2bpz-gwpy
- Relevé détaillé des consommations des bâtiments pour
l’année 2016
- 3376 bâtiments, 46 colonnes descriptives
- Descriptif des champs du jeu de donnée

## III.5) Librairies
Jupyter Notebook, Python, Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn, Scipy



# IV) Segmentation clients e commerce

## IV.1) Contexte  
- Projet de segmentation des Clients du site d’E-commerce Olist
- Olist a besoin d’une segmentation de ses clients à utiliser au quotidien pour ses campagnes de communication

## IV.2) But
- Créer une segmentation Client pour l’équipe Marketing ainsi qu’une proposition de contrat de maintenance

## IV.3) Objectifs
- Traiter et explorer le jeu de donnée
- Réaliser des modélisations de segmentation
- Evaluer les modèles
- Proposer la ou les segmentations pertinentes
- Proposer une maintenance adaptée

## IV.4) Le jeu de données
- Le jeu de données https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- Base de données Client anonymisée
- 8 jeux de données

## IV.5) Librairies
Jupyter Notebook, Python, Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn


# V) Classification des biens de consommation

## V.1) Contexte  
- Projet de lancement d’un site de E-commerce pour la société « Place demarché ».
Attribution de la catégorie des articles manuelle par les vendeurs = peu fiable, pas adapté à un volume d’articles important

## V.2) But
-  Etudier la faisabilité d’un moteur de classification des articles par catégories, à partir du texte et de l’image

## V.3) Objectifs
- Etudier la faisabilité d’un moteur de classification avec le texte
- Etudier la faisabilité d’un moteur de classification avec les images
- Réaliser une classification supervisée à partir des images
- Tester la collecte de produits via une API

## V.4) Le jeu de données
- Le jeu de données : flipkart_com-ecommerce_sample_1050.csv
- 1050 images au format jpg
- 7 catégories avec répartition homogène :
• Home Furnishing
• Baby Care
• Watches
• Home Decor & Festive Needs
• Kitchen & Dining
• Beauty and Personal Care
• Computers

## V.5) Librairies 
Jupyter Notebook, Python, Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn, re, nltk, os, imread, keras, tensorflow



# VI) Modèle de scoring

## VI.1) Contexte  
- Projet de mise en œuvre d’un outil de «scoring credit»
 = probabilité qu’un client rembourse son crédit
 = classification de la demande en « accordée » ou « refusée ».
- Proposition de crédits à la consommation pour des personnes ayant peu oupas du tout d’historique de prêt
= Risque financier important pour l’entreprise Prêt à dépenser

## VI.2) But
-  Développer et mettre en production un modèle de scoring pour prédire la probabilité de faillite d’un client, et sa classification en « refusé » ou « accepté », avec une démarche MLOPS


## VI.3) Objectifs
- Réaliser une analyse exploratoire et sélectionner les variables pertinentes
- Modéliser, optimiser et choisir le meilleur modèle
- Analyser l’impact des variables retenues
- Réaliser une API et la déployer avec les tests associés
- Analyser en production le datadrift

## VI.4) Le jeu de données
- Le jeu de données : 8 fichiers csv + 1 de description
- application_train.csv
= 122 colonnes, 307511 lignes
- application_test.csv
= 121 colonnes, 48744 lignes
- bureau_balance.csv
= 17 colonnes, 1716428 lignes
- bureau.csv
= 3 colonnes, 27299924 lignes
- POS_CASH_balance.csv
= 8 colonnes, 10001357 lignes
- instalments_payments.csv
= 8 colonnes, 13605400 lignes
- credit_card_balance.csv
= 23 colonnes, 3840311 lignes
- previous_application.csv
= 37 colonnes, 1670213 lignes

## VI.5) Librairies 
Jupyter Notebook, Python, Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn, imblearn, time, mlflow, lightgbm, shap, joblib, fastapi


# VII) Dashboard

## VII.1) Contexte  
- Projet de mise en œuvre d’un outil de «scoring credit»
 = probabilité qu’un client rembourse son crédit
 = classification de la demande en « accordée » ou « refusée ».
- Proposition de crédits à la consommation pour des personnes ayant peu oupas du tout d’historique de prêt
= Risque financier important pour l’entreprise Prêt à dépenser

## VII.2) But
-  Réaliser un dashboard interactif et le déployer sur le cloud, et réaliser une veille technique


## VII.3) Objectifs
- À partir du projet précèdent élaborer un dashboard avec streamlit
- Respecter le principe WCAG
- Tester et déployer le dashboard avec strealmit io
- Réaliser une veille technique sur le vision transformer (vit)
- Réaliser un POC
- Réaliser une note technique

## VII.4) Le jeu de données
- SO

## VII.5) Librairies 
Jupyter Notebook, Python, Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn, imblearn, time, mlflow, lightgbm, shap, joblib, fastapi, streamlit



# VIII) Traitement AWS

## VIII.1) Contexte  
- solutions innovantes pour la récolte de fruits
- application mobile avec prise de photo et identification du fruit
= Sensibiliser à la diversité des fruits
= Première version du moteur de classification des images de fruits
= Travaux de traitement initial réalisés et à utiliser

## VIII.2) But
-  Réaliser une démonstration de la mise en place d’une instance EMR opérationnelle


## VIII.3) Objectifs
- S’approprier le travail déjà réalisé
- Respecter le principe RGPD
- Mettre en œuvre une solution de traitement en local
- Préparer l’environnement de traitement big data
- Mettre en œuvre la solution de traitement via une instance EMR
- Réaliser une conclusion

## VIII.4) Le jeu de données
- https://www.kaggle.com/datasets/moltean/fruits

## VIII.5) Librairies 
Google colab, pyspark, pyarrow, io, os, tensorflow, Jupiter Notebook, Python, pandas, numpy, AWS, S3, ECS, EMR, AWS CLI, pyspark, pyarrow, io, os, tensorflow, JupiterHub
