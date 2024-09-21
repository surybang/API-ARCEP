# preprocess.py

import pandas as pd


def preprocess_data(input_file):
    """
    Cette fonction permet de prétraiter les données du fichier CSV en ajoutant un 0
    au début de chaque observation dans la colonne EZABPQM. La colonne est convertit
    en String par la même occasion.

    Args:
        input_file (str): Le fichier CSV à prétraiter
    """

    try:
        df = pd.read_csv(input_file, sep=";", encoding="utf-8")

        if "EZABPQM" in df.columns:
            # Convertir la colonne en string + ajouter un 0 à chaque obs. avec un lambda
            df["EZABPQM"] = df["EZABPQM"].astype(str).apply(lambda x: "0" + x)
            # print(df.head())
            # print("Types de colonnes après conversion :")
            # print(df.dtypes)

            df.to_csv(input_file, sep=";", encoding="utf-8", index=False)
            print(f"Les données dans {input_file} ont été prétraitées avec succès")
        else:
            print(f"La colonne EZABPQM n'existe pas dans {input_file}")
    except Exception as e:
        print(f"Erreur lors du prétraitement des données dans {input_file}: {e}")
        raise


def preprocess_dates(df: pd.DataFrame, date_columns: str) -> pd.DataFrame:
    """Cette fonction permet de transformer une colonne date dans le format attendu par DuckDB

    Args:
        df (pd.DataFrame): le dataframe à transformer
        date_columns (str): la colonne du dataframe à transformer

    Returns:
        pd.DataFrame: le dataframe transformé avec sa colonne au format attendu
    """
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], format="%d/%m/%Y").dt.strftime("%Y-%m-%d")
    return df
