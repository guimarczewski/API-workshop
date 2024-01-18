import pytest

from fastapi.testclient import TestClient

from API.app.main import app

client = TestClient(app)

def test_ola_mundo():
    response = client.get("/")
    assert response.status_code == 200

def test_ola_mundo_json():
    response = client.get("/")
    assert response.json() == {"Hello":"World"}

def test_listar_produtos_status_code():
    response = client.get("/produtos")
    assert response.status_code == 200

def test_tamanho_lista_produtos():
    response = client.get("/produtos")
    assert len(response.json()) == 3

def teste_pega_um_produto():
    response = client.get("/produtos/1")
    assert response.json() == {
        "id":1,
        "nome":"Smartphone",
        "descricao":"Um telefone inteligente",
        "preco":1500.00
    }