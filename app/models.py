import duckdb
from .config import config
import pandas as pd


def convert_to_utf8(input_file, output_file):
    """Cette fonction permet de convertir l'encodage d'un fichier csv

    Args:
        input_file (csv origine): Fichier csv dans son format encoding d'origine
        output_file (csv utf8): Fichier csv dans son nouveau format encoding utf-8
    """
    try:
        df = pd.read_csv(
            input_file,
            sep=config["data"]["separator"],
            encoding=config["data"]["encoding"],
        )
        df.to_csv(
            output_file, sep=config["data"]["separator"], encoding="utf-8", index=False
        )
        print(f"Fichier {input_file} converti en {output_file} avec l'encodage UTF-8")
    except Exception as e:
        print(f"Erreur lors de la conversion {input_file} en UTF-8 : {e}")
        raise

def preprocess_data(input_file):
    """
    Cette fonction permet de prétraiter les données du fichier CSV en ajoutant un 0
    au début de chaque observation dans la colonne EZABPQM. La colonne est convertit
    en String par la même occasion.

    Args:
        input_file (str): Le fichier CSV à prétraiter
    """

    try :
        df = pd.read_csv(
            input_file,
            sep=";",
            encoding="utf-8"
        )

        if "EZABPQM" in df.columns:
            # Convertir la colonne en string + ajouter un 0 à chaque obs. avec un lambda
            df["EZABPQM"] = df["EZABPQM"].astype(str).apply(lambda x: '0'+x)
            # print(df.head())
            print("Types de colonnes après conversion :")
            print(df.dtypes)

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
        df[col] = pd.to_datetime(df[col], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
    return df



def init_database():
    """
    Cette fonction permet d'initialiser la base de données DuckDB
    Elle convertit dans un premier temps les fichiers *.csv vers un encoding utf-8
    avec la fonction convert_to_utf8().
    Elle crée dans un second temps les tables MAJNUM et R1R2. 
    """
    try:
        # Récupérer les données et convertir en utf8
        convert_to_utf8(config["data"]["url_num"], "MAJNUM_utf8.csv")
        convert_to_utf8(config["data"]["url_r1r2"], "MAJR1R2_utf8.csv")

        # Transformer EZABPQM en String en rajoutant un 0 devant
        preprocess_data("MAJNUM_utf8.csv")
        

        # Charger les données dans duckdb
        con = duckdb.connect(config["database"]["path"])
        df_num = pd.read_csv(
            "MAJNUM_utf8.csv", sep=config["data"]["separator"], encoding="utf-8", dtype={'EZABPQM': str}
        )
        df_r1r2 = pd.read_csv(
            "MAJR1R2_utf8.csv", sep=config["data"]["separator"], encoding="utf-8"
        )
        df_num = preprocess_dates(df_num, ["Date_Attribution"])
        df_r1r2 = preprocess_dates(df_r1r2, ["Date d'effet (attribution)"])
        

        # Connexion à DuckDB
        con = duckdb.connect(config["database"]["path"])

        con.execute("""
            CREATE TABLE IF NOT EXISTS MAJNUM (
                    EZABPQM VARCHAR,
                    Tranche_Debut BIGINT,
                    Tranche_Fin BIGINT, 
                    Mnémo VARCHAR,
                    Territoire VARCHAR,
                    Date_attribution DATE
                    )
                    """)
        con.execute("INSERT INTO MAJNUM SELECT * from df_num;")
        con.execute("CREATE TABLE IF NOT EXISTS R1R2 AS SELECT * FROM df_r1r2;")
        con.close()

        print("Base de données initialisées avec succès")
    except Exception as e:
        print(f"Erreur lors de l'initialisation de la base de données {e}")
        raise


def merged_data():
    con = duckdb.connect(config['database']['path'])

    df_num = con.execute("SELECT EZABPQM::VARCHAR AS EZABPQM, Mnémo FROM MAJNUM ;").fetchdf()
    df_r1r2 = con.execute("SELECT 'Code attributaire', Attributaire FROM R1R2 ;").fetchdf()
    print("Les types pour df_num :")
    print(df_num.dtypes)
    print("\n les types pour df_r1r2 :")
    print(df_r1r2.dtypes)
    print(df_num.head())




def get_majnum():
    con = duckdb.connect(config["database"]["path"])
    result = con.execute("SELECT * from MAJNUM").fetchdf()
    con.close()
    return result


def get_r1r2():
    con = duckdb.connect(config["database"]["path"])
    result = con.execute("SELECT * from r1r2").fetchdf()
    con.close()
    return result
