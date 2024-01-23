import pytest

from fastapi.testclient import TestClient

from app.main import app

from dotenv import load_dotenv

load_dotenv()
# load_dotenv(dotenv_path="API/.env-prod")

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

print(db_port)

client = TestClient(app)

def test_ola_mundo():
    response = client.get("/")
    assert response.status_code == 200

def test_listar_produtos_status_code():
    response = client.get("/produtos")
    assert response.status_code == 200