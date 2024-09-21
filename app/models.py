# models.py
import os
import duckdb
from .config import config, DATABASE_PATH
import pandas as pd


def get_search_data(input_user: str) -> dict:
    con = duckdb.connect(DATABASE_PATH)
    try:
        input_length = len(input_user)

        q = f"""
        SELECT EZABPQM, "Code Attributaire", Attributaire
        FROM SEARCH_TABLE
        WHERE LEFT(EZABPQM, ?) = ? ; 
        """
        result = con.execute(q, (input_length, input_user)).fetchdf()
        # print(result.head())
        # print(len(result))

        if len(result) == 0:
            return {
                "status": "error",
                "message": "Aucun identifiant trouvé",
            }
        elif len(result) == 1:
            results = result.to_dict(orient="records")
            return {
                "status": "success",
                "data": results,
            }
        else:
            results = result.to_dict(orient="records")
            return {
                "status": "warning",
                "message": "Plusieurs résultats correspondent à la recherche, vous pouvez saisir un identifiant plus précis si vous le souhaitez",
                "data": results,
            }
    finally:
        con.close()


def get_majnum_data() -> dict:
    con = duckdb.connect(DATABASE_PATH)
    result = con.execute("SELECT * from MAJNUM").fetchdf()
    con.close()
    return result.to_dict(orient="records")


def get_r1r2_data() -> dict:
    con = duckdb.connect(DATABASE_PATH)
    result = con.execute("SELECT * from r1r2").fetchdf()
    con.close()
    return result.to_dict(orient="records")


def get_nom_attributaire() -> dict:
    con = duckdb.connect(DATABASE_PATH) 
    q = """
        SELECT DISTINCT "Code attributaire", Attributaire from SEARCH_TABLE;
        """
    result = con.execute(q).fetch_df()
    con.close()
    results = result.to_dict(orient="records")
    return {
        "data": results,
    }


def get_attributaire(input_user: str) -> dict:
    con = duckdb.connect(DATABASE_PATH)
    q = """
        SELECT * FROM SEARCH_TABLE WHERE UPPER("Code Attributaire") = UPPER(?)
        """
    result = con.execute(q, (input_user,)).fetchdf()
    con.close()
    results = result.to_dict(orient="records")
    return {
        "status": "success",
        "data": results,
    }
