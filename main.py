from fastapi import FastAPI

app = FastAPI()

# vamos criar as rotas que são os endereços
@app.get("/") # request
def ola_mundo(): # response
    return {"ola":"mundo"}