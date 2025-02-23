import pytest
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from .list_person_controller import ListPersonController

class MockPessoaFisica:
    def __init__(self,id,renda_mensal,idade,nome_completo,celular,email,categoria,saldo):
        self.id = id
        self.renda_mensal = renda_mensal
        self.idade = idade
        self.nome_completo = nome_completo
        self.celular = celular
        self.email = email
        self.categoria = categoria
        self.saldo = saldo

class MockPessoaFisicaRepository:
    def get(self):
        return [
            {
                "renda_mensal": 2000,
                "idade": 30,
                "nome_completo": "Jhon Doe",
                "celular": "96369-9691",
                "email": "teste@teste.com",
                "categoria": "Categoria A",
                "saldo": 5000
            }
        ]
    
class MockPessoaJuridicaRepository:
    def get(self):
        return [
            {
            "faturamento": 80000,
            "idade": 10,
            "nome_fantasia": "JD Bussiness LTDA",
            "celular": "96369-9691",
            "email_corporativo": "teste@teste.com",
            "categoria": "Categoria B",
            "saldo": 500000
            }
        ]
    
def test_list_pessoa_fisica():
    controller = ListPersonController(MockPessoaFisicaRepository(),MockPessoaJuridicaRepository())

    response = controller.list_person("PF")

    expected_response = {
        "data": {
                "type": "Pessoa Fisica",
                "count": 1,
                "attributes": [{
                    "renda_mensal": 2000,
                    "idade": 30,
                    "nome_completo": "Jhon Doe",
                    "celular": "96369-9691",
                    "email": "teste@teste.com",
                    "categoria": "Categoria A",
                    "saldo": 5000
                }]
            }
    }

    assert response == expected_response

def test_list_pessoa_juridica():
    controller = ListPersonController(MockPessoaFisicaRepository(),MockPessoaJuridicaRepository())

    response = controller.list_person("PJ")

    expected_response = {
        "data": {
                "type": "Pessoa Juridica",
                "count": 1,
                "attributes": [{
                    "faturamento": 80000,
                    "idade": 10,
                    "nome_fantasia": "JD Bussiness LTDA",
                    "celular": "96369-9691",
                    "email_corporativo": "teste@teste.com",
                    "categoria": "Categoria B",
                    "saldo": 500000
                }]
            }
    }

    assert response == expected_response

def test_list_pessoa_erro():
    controller = ListPersonController(MockPessoaFisicaRepository(),MockPessoaJuridicaRepository())

    with pytest.raises(Exception):
        controller.list_person("TYPE")