from fastapi import FastAPI
from typing import List, Dict

# importar classes - coloca o ponto antes pois está no mesmo repositorio
from .schema import ProdutosSchema
from .data import Produtos

app = FastAPI()
lista_de_produtos = Produtos()

# vamos criar as rotas que são os endereços
@app.get("/") # request
def ola_mundo(): # response
    return {"Hello":"World"}

@app.get("/produtos", response_model=list[ProdutosSchema]) # request definindo qual schema a lista de saída precisa ter
def listar_produtos():
    return lista_de_produtos.listar_produtos()

# endpoint para pegar os produtos
@app.get("/produtos/{id}", response_model=ProdutosSchema) # request
def buscar_produto(id: int): # response
    return lista_de_produtos.buscar_produto(id)

@app.post("/produtos", response_model=list[ProdutosSchema])
def adicionar_produto(produto: ProdutosSchema):
    return produto.adicionar_produto(produto.model_dump())