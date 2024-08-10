import duckdb
from .config import config
import pandas as pd


def convert_to_utf8(input_file, output_file):
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


def init_database():
    try:
        # Récupérer les données et convertir en utf8
        convert_to_utf8(config["data"]["url_num"], "MAJNUM_utf8.csv")
        convert_to_utf8(config["data"]["url_r1r2"], "MAJR1R2_utf8.csv")

        # Charger les données dans duckdb
        con = duckdb.connect(config["database"]["path"])
        df_num = pd.read_csv(
            "MAJNUM_utf8.csv", sep=config["data"]["separator"], encoding="utf-8"
        )
        df_r1r2 = pd.read_csv(
            "MAJR1R2_utf8.csv", sep=config["data"]["separator"], encoding="utf-8"
        )

        # Connexion à DuckDB
        con = duckdb.connect(config["database"]["path"])

        con.execute("CREATE TABLE IF NOT EXISTS MAJNUM AS SELECT * FROM df_num;")
        con.execute("CREATE TABLE IF NOT EXISTS R1R2 AS SELECT * FROM df_r1r2;")
        con.close()

        print("Base de données initialisées avec succès")
    except Exception as e:
        print(f"Erreur lors de l'initialisation de la base de données {e}")
        raise


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
