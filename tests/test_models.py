# test/test_models.py
from unittest.mock import patch
from app.models import get_search_data, get_attributaire
import pandas as pd

@patch('app.models.duckdb.connect')
def test_get_search_data(mock_connect):
    # Simuler le retour de la base de données
    mock_con = mock_connect.return_value
    mock_df = pd.DataFrame ({
        'EZABPQM' : ['06298'],
        'Code Attributaire': ['SFR0'],
        'Attributaire' : ['Société française du radiotéléphone']
    })
    # Simuler le retour de la méthode fetchdf()
    mock_con.execute.return_value.fetchdf.return_value = mock_df

    # Appeler la fonction avec un identifiant utilisateur simulé
    response = get_search_data('06298')

    # Vérifier que la réponse contient les données attendues
    assert response['status'] == 'success'
    assert len(response['data']) == 1
    assert response['data'][0]['EZABPQM'] == '06298'

@patch('app.models.duckdb.connect')
def test_get_search_data_no_result(mock_connect):
    mock_con = mock_connect.return_value
    mock_df = pd.DataFrame(
        columns=['EZABPQM', 'Code Attributaire', 'Attributaire']
    )

    mock_con.execute.return_value.fetchdf.return_value = mock_df
    response = get_search_data('0000')
    assert response['status'] == 'error'
    assert response['message'] == 'Aucun identifiant trouvé'

@patch('app.models.duckdb.connect')
def test_get_attributaire(mock_connect):
    # Simuler un DataFrame pandas avec les valeurs attendues
    mock_con = mock_connect.return_value
    mock_df = pd.DataFrame({
        'EZABPQM': ['07484', '07485', '0774', '06028', '07486', '06029', '0773', '07482', '07483'],
        'Code Attributaire': ['SMAA'] * 9,
        'Attributaire': ['Syma'] * 9
    })

    # Simuler le retour de la méthode fetchdf()
    mock_con.execute.return_value.fetchdf.return_value = mock_df

    # Appeler la fonction avec un identifiant utilisateur simulé
    response = get_attributaire('SMAA')

    # Vérifier que la réponse contient les données attendues
    assert response['status'] == 'success'
    assert len(response['data']) == 9
    assert response['data'][0]['EZABPQM'] == '07484'
    assert response['data'][0]['Code Attributaire'] == 'SMAA'
    assert response['data'][0]['Attributaire'] == 'Syma'