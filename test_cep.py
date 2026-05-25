import pytest
import requests

# Parte 2 - arquitetura dos testes

@pytest.fixture(scope='session') #fixture de sessão - cliente http
def api_client():
    session = requests.Session()
    yield session
    session.close()

@pytest.fixture(scope='function') #fixture de função - rastreador de performace
def base_url():
    return "https://viacep.com.br/ws/"

# Parte 3 - implementação

def test_cep_valido(api_client, base_url):
    cep = "01001000"
    response = api_client.get(f"{base_url}{cep}/json/")

    assert response.status_code == 200
    data = response.json()
    assert "erro" not in data
    assert "logradouro" in data and len(data["logradouro"]) > 0
    assert "bairro" in data and len(data["bairro"]) > 0
    assert "localidade" in data and len(data["localidade"]) > 0
    assert "uf" in data and len(data["uf"]) > 0


def test_cep_inexistente(api_client, base_url):
    cep = "99999999"
    response = api_client.get(f"{base_url}{cep}/json/")
    
    assert response.status_code == 200
    data = response.json()
    assert data["erro"] is True or data["erro"] == "true"


def test_formato_invalido(api_client, base_url):
    cep = "ABCDE-XYZ"
    response = api_client.get(f"{base_url}{cep}/json/")
    
    assert response.status_code == 400


def test_cep_com_espacos(api_client, base_url):
    cep = "01001 000"
    response = api_client.get(f"{base_url}{cep}/json/")
    
    assert response.status_code == 400


def test_cep_com_hifen(api_client, base_url):

    cep = "01001-000"
    response = api_client.get(f"{base_url}{cep}/json/")
    
    assert response.status_code == 200
    data = response.json()
    assert data["logradouro"] == "Praça da Sé"


def test_cep_incompleto(api_client, base_url):
    cep = "123"
    response = api_client.get(f"{base_url}{cep}/json/")
    
    assert response.status_code == 400