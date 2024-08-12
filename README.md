# 📞 Recherche Opérateur Téléphonique

Bienvenue dans le projet **Recherche Opérateur Téléphonique** ! 

Ce projet permet de rechercher des informations sur les opérateurs téléphoniques en France, en se basant sur les données fournies par l'ARCEP. Nous avons mis en place une API  avec FastAPI, accompagnée d'une interface utilisateur développée avec Streamlit.

## 📝 Description

Ce projet a pour but de permettre la recherche de l'opérateur téléphonique associé à un numéro de téléphone ou un nom d'opérateur donné. Les données proviennent de l'ARCEP, l'autorité française de régulation des communications électroniques et des postes. 

### 🔍 Fonctionnalités principales

- **Recherche par numéro de téléphone** : Entrez un numéro de téléphone pour découvrir l'opérateur associé.
- **Recherche par nom d'opérateur** : Recherchez des informations en entrant le nom ou le code d'un opérateur.
- **API FastAPI** : Une API RESTful construite avec FastAPI pour servir les données.
- **Interface utilisateur Streamlit** : Une interface pour effectuer des recherches via un navigateur web.

## 🚀 Fonctionnement du Projet

### 1. Collecte des Données

Les données sont récupérées depuis le site de l'ARCEP. Elles incluent les informations sur les codes d'attribution des numéros ainsi que les noms des opérateurs correspondants.

### 2. Nettoyage et Stockage

Les données brutes sont nettoyées, puis stockées dans une base de données DuckDB. Une jointure est effectuée pour associer chaque numéro de téléphone à son opérateur en utilisant les codes d'attribution.

### 3. API FastAPI

L'API FastAPI sert les données nettoyées et jointes. Elle permet de rechercher les opérateurs par numéro de téléphone ou par nom d'opérateur.

### 4. Interface Utilisateur Streamlit

Streamlit est utilisé pour créer une interface simple et efficace permettant aux utilisateurs de rechercher facilement des informations sur les opérateurs téléphoniques.

## 🛠️ Installation

### Prérequis

- Python 3.8 ou supérieur
- `pip` pour l'installation des dépendances

### Étapes d'installation

1. **Clonez le dépôt** :

   ```bash
   git clone https://github.com/votre-utilisateur/recherche-operateur-telephonique.git
   cd recherche-operateur-telephonique

2. ** Créez un environnement virtuel** :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`

3. **Installez les dépendances** :

   ```bash
   pip install -r requirements.txt

4. **Lancez le script d'initialisation** :

   Ce script permet d'initialiser la base de données et de lancer les services (FastAPI & Streamlit)

   ```bash
   chmod+x starter.sh
   ./starter.sh

## 📊 Utilisation

### Interface Web

1. **Connectez-vous à l'interface utilisateur** :
   - Ouvrez votre navigateur web et rendez-vous à l'adresse suivante après avoir démarré l'application :
   
     ```bash
     127.0.0.1:8501
     ```
   
2. **Effectuez une recherche** :
   - Entrez un numéro de téléphone ou un code d'opérateur dans le champ de recherche pour obtenir les informations associées.

### API

1. **Accédez à l'API** :
   - L'API est disponible à l'adresse suivante :
   
     ```bash
     http://127.0.0.1:8000/docs
     ```



