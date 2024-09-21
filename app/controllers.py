# controllers.py
from fastapi import APIRouter, HTTPException
from .models import get_search_data, get_r1r2_data, get_majnum_data, get_attributaire, get_nom_attributaire

router = APIRouter()


@router.get("/search/{input_user}")
def search_identifiant(input_user: str) -> dict:
    """
    Route pour récupérer l'identifiant saisi d'un numéro de téléphone saisi par l'user

    Args:
        input_user (str): numéro de téléphone
    Returns:
        result (dict): Un dictionnaire contenant le statu et les données ou un message.
    """

    try:
        response = get_search_data(input_user)
        if response["status"] == "error":
            raise HTTPException(status_code=404, detail=response["message"])
        elif response["status"] == "warning":
            return {
                "status": response["status"],
                "message": response["message"],
                "data": response["data"],
            }
        else:
            return {
                "status": response["status"],
                "data": response["data"],
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/nom_attributaire")
def get_attributaire_data() -> dict:
    try:
        response = get_nom_attributaire()
        return {
            "data": response["data"]
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        


@router.get("/attributaire/{input_user}")
def search_attributaire(input_user: str) -> dict:
    try :
        response = get_attributaire(input_user)
        if response["status"] == "success":
            return {
                "status": response["status"],
                "data": response["data"],
            }
        else:
            raise HTTPException(status_code=404)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
