#!/bin/bash

echo "Initialisation de la base de données..."
python initialize_db.py

echo "Lancement de l'API FastAPI..."
uvicorn app.main:app --reload &

echo "Lancement de l'application Streamlit..."
streamlit run streamlit_app.py

echo "Tous les services sont lancés."

