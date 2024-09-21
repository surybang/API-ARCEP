from fastapi.testclient import TestClient
import httpx
from app.main import app
from unittest.mock import patch
from app.controllers import search_identifiant

client = TestClient(app)

@patch('app.controllers.search_identifiant')
def test_search_identifiant_success(mock_get_search_data):
    # Simuler une réponse réussie de get_search_data
    mock_get_search_data.return_value = {
        "status": "success",
        "data": [
            {
                "EZABPQM": "06298",
                "Code Attributaire": "SFR0",
                "Attributaire": "Société française du radiotéléphone"
            }
        ]
    }

    # Faire une requête GET à la route /search/{input_user}
    response = client.get("/search/06298")
    
    # Vérifier que la réponse est correcte
    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "data": [
            {
                "EZABPQM": "06298",
                "Code Attributaire": "SFR0",
                "Attributaire": "Société française du radiotéléphone"
            }
        ]
    }

@patch('app.models.get_search_data')
def test_search_identifiant_not_found(mock_get_search_data):
    # Simuler une réponse avec une erreur
    mock_get_search_data.return_value = {
        "status": "error",
        "message": "Aucun identifiant trouvé"
    }

    # Faire une requête GET à la route /search/{input_user}
    response = client.get("/search/00000")
    
    # Vérifier que la réponse est correcte
    assert response.status_code == 404
    assert response.json() == {
        "detail": 'Aucun identifiant trouvé'
    }