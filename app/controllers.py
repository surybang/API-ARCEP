from fastapi import APIRouter, HTTPException
from models import get_search_data, get_r1r2_data, get_majnum_data

router = APIRouter()


@router.post("/search/{input_user}")
def search_identifiant(input_user: str) -> str:
    """
    Route pour récupérer l'identifiant saisi d'un numéro de téléphone saisi par l'user

    Args:
        input_user (str): numéro de téléphone
    Returns:
        result (str): l'identifiant du numéro
    """

    try:
        result = get_search_data(input_user)
        if "Aucun identifiant trouvé" in result:
            raise HTTPException(status_code=404, detail=result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    