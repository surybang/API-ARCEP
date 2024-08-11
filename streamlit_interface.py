# Streamlit interface
import streamlit as st
import requests
from app.config import HOST_PATH, PORT_PATH
import pandas as pd

st.title("Rechercher un opérateur téléphonique")

input_user = st.text_input("Entrez un numéro de téléphone portable:")

if st.button("Rechercher"):
    if input_user:
        try:
            response = requests.get(
                f"http://{HOST_PATH}:{PORT_PATH}/search/{input_user}"
            )
            response_data = response.json()
            if response.status_code == 200:
                if response_data["status"] == "success":
                    df = pd.DataFrame(response_data['data'])
                    st.dataframe(df)

                elif response_data["status"] == "warning":
                    st.warning(f"{response_data['message']}")
                    df2 = pd.DataFrame(response_data['data'])
                    st.dataframe(df2)

            else:
                st.error(f"Erreur {response.json()['detail']}")
        except requests.exceptions.RequestException as e:
            st.error(f"Erreur de connexion à l'API : {str(e)}")
    else:
        st.warning("Veuillez entrer un numéro de téléphone.")
