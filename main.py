from fastapi import FastAPI

app = FastAPI(title="Ton Pote Musclé API", description="API pour la gestion des utilisateurs et des entraînements", version="1.0.0")

@app.get("/")
def read_root():
    return {"Hello": "World"}