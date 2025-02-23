import pytest
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from .extract_controller import ExtractController

class MockPessoaFisicaRepository:
    def get_pessoa_fisica(self, pessoa_fisica_id: int) -> PessoaFisica:
        return {
                "renda_mensal": 2000,
                "idade": 30,
                "nome_completo": "Jhon Doe",
                "celular": "96369-9691",
                "email": "teste@teste.com",
                "categoria": "Categoria A",
                "saldo": 5000
        }

class MockPessoaJuridicaRepository:
    def get_pessoa_juridica(self, pessoa_juridica_id: int) -> PessoaJuridica:
        return {
            "faturamento": 80000,
            "idade": 10,
            "nome_fantasia": "JD Bussiness LTDA",
            "celular": "96369-9691",
            "email_corporativo": "teste@teste.com",
            "categoria": "Categoria B",
            "saldo": 50000
            }
    
class MockPessoaFisicaNotFoundRepository:
    def get_pessoa_fisica(self, pessoa_fisica_id: int) -> PessoaFisica:
        return None

class MockPessoaJuridicaNotFoundRepository:
    def get_pessoa_juridica(self, pessoa_juridica_id: int) -> PessoaJuridica:
        return None

def test_widraw_money_client_pf_not_found():
    controller = ExtractController(MockPessoaFisicaNotFoundRepository(), MockPessoaJuridicaNotFoundRepository())

    with pytest.raises(Exception) as exc_info:
        controller.extract(1,"PF")

    assert str(exc_info.value) == "Cliente não encontrado"

def test_widraw_money_client_pf():
    controller = ExtractController(MockPessoaFisicaRepository(), MockPessoaJuridicaRepository())

    response = controller.extract(1,"PF")

    expected_response = {
            "data": {
                "type": "Pessoa Fisica",
                "count": 1,
                "attributes": {
                    "name": "Jhon Doe",
                    "balance": 5000,
                    "type": "Pessoa Fisica"
                }
            }
        }
    
    assert response == expected_response

def test_widraw_money_client_pj_not_found():
    controller = ExtractController(MockPessoaFisicaNotFoundRepository(), MockPessoaJuridicaNotFoundRepository())

    with pytest.raises(Exception) as exc_info:
        controller.extract(1,"PJ")

    assert str(exc_info.value) == "Cliente não encontrado"

def test_widraw_money_client_pj():
    controller = ExtractController(MockPessoaFisicaRepository(), MockPessoaJuridicaRepository())

    response = controller.extract(1,"PJ")

    expected_response = {
            "data": {
                "type": "Pessoa Juridica",
                "count": 1,
                "attributes": {
                    "name": "JD Bussiness LTDA",
                    "balance": 50000,
                    "type": "Pessoa Juridica"
                }
            }
        }
    
    assert response == expected_response
