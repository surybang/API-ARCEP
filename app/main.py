from fastapi import FastAPI
from .controllers import router
from .config import HOST_PATH, PORT_PATH

app = FastAPI()

app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API FastAPI"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=HOST_PATH, port=PORT_PATH)
