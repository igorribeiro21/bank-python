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
        list_get = []
        pessoa_fisica = MockPessoaFisica(
            id=1,
            renda_mensal=2000,
            idade=30,
            nome_completo="Jhon Doe",
            celular="96369-9691",
            email="teste@teste.com",
            categoria="Categoria A",
            saldo=5000
        )

        list_get.append(pessoa_fisica)

        return list_get
    
class MockPessoaJuridicaRepository:
    def get(self):
        list_get = []
        pessoa_fisica = MockPessoaFisica(
            renda_mensal=2000,
            idade=30,
            nome_completo="Jhon Doe",
            celular="96369-9691",
            email="teste@teste.com",
            categoria="Categoria A",
            saldo=5000
        )

        list_get.append(pessoa_fisica)

        return list_get
    
def test_list_person_pessoa_fisica():
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
    