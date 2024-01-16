from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

# criar lista de produtos com str - chave - e any - valor, descricao, bool
produtos: List[Dict[str, any]] = [

    {
        "id":1,
        "nome":"Smartphone",
        "descricao":"Um telefone inteligente",
        "preco":1500.00
    },
    {
        "id":2,
        "nome":"Notebook",
        "descricao":"Computador gamer",
        "preco":3500.00
    },
    {
        "id":3,
        "nome":"Tablet",
        "descricao":"Um computador movel",
        "preco":2500.00
    }
]

# vamos criar as rotas que são os endereços
@app.get("/") # request
def ola_mundo(): # response
    return {"Hello":"World"}

@app.get("/produtos") # request
def listar_produtos(): # response
    return produtos