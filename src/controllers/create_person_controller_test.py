# import pytest
from .create_person_controller import CreatePersonController

class MockPessoaFisicaRepository:
    def create(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str,categoria: str, saldo:float) -> None:
        pass

class MockPessoaJuridicaRepository:
    def create(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str,categoria: str, saldo:float) -> None:
        pass

def test_create_pessoa_fisica():
    person_info = {
        "type": "PF",
        "renda_mensal": 5000,
        "idade": 30,
        "nome_completo": "Jhon Doe",
        "celular": "99635-6596",
        "email": "teste@teste.com",
        "categoria": "Categoria A",
        "saldo": 15000.00
    }

    controller = CreatePersonController(MockPessoaFisicaRepository(), MockPessoaFisicaRepository())

    response = controller.create(person_info)

    assert response["data"]["type"] == "Pessoa Fisica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def test_create_pessoa_juridica():
    person_info = {
        "type": "PJ",
        "faturamento": 15000,
        "idade": 30,
        "nome_fantasia": "JD Bussines LTDA",
        "celular": "99635-6596",
        "email_corporativo": "teste@teste.com",
        "categoria": "Categoria B",
        "saldo": 150000.00
    }

    controller = CreatePersonController(MockPessoaFisicaRepository(), MockPessoaFisicaRepository())

    response = controller.create(person_info)

    assert response["data"]["type"] == "Pessoa Fisica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info
