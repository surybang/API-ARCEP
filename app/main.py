from fastapi import FastAPI
from controllers import router
from config import config

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API FastAPI"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=config["api"]["host"], port=config["api"]["port"])
