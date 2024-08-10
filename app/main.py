from fastapi import FastAPI
from app.controllers import get_majnum_data, get_r1r2_data, search_data
from .config import config

app = FastAPI()

# Route pour récupérer les données de la table MAJNUM
@app.get("/majnum")
def majnum_route():
    return get_majnum_data()

# Route pour récupérer les données de la table R1R2
@app.get("/r1r2")
def r1r2_route():
    return get_r1r2_data()

@app.get('/search')
def search_route():
    return search_data()



# Point de départ de l'application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config['api']['host'], port=config['api']['port'])