# Image de base Python
FROM python:3.10

# Récupérer le dossier de travail
WORKDIR /api-arcep

# Copier tout le contenu 
COPY . .

# Ajouter le répertoire de travail au PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:/api-arcep"

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Ajouter les droits d'exec au script starter.sh
RUN chmod +x starter.sh

# Exposer les ports pour fastapi et streamlit
EXPOSE 8000 8501

# Lancer le script 
CMD ["./starter.sh"]