from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
import pytest
from .withdraw_money_controller import WithdrawMoneyController

class MockPessoaFisicaRepository:
    def update_saldo(self, pessoa_fisica_id: int, saldo: float) -> None:
        pass

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
    def update_saldo(self, pessoa_juridica_id: int, faturamento: float) -> None:
        pass

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
    def update_saldo(self, pessoa_fisica_id: int, saldo: float) -> None:
        pass

    def get_pessoa_fisica(self, pessoa_fisica_id: int) -> PessoaFisica:
        return None

class MockPessoaJuridicaNotFoundRepository:
    def update_saldo(self, pessoa_juridica_id: int, faturamento: float) -> None:
        pass

    def get_pessoa_juridica(self, pessoa_juridica_id: int) -> PessoaJuridica:
        return None

def test_widraw_money_client_pf_not_found():
    controller = WithdrawMoneyController(MockPessoaFisicaNotFoundRepository(), MockPessoaJuridicaNotFoundRepository())

    with pytest.raises(Exception) as exc_info:
        controller.withdraw_money(100,1,"PF")

    assert str(exc_info.value) == "Cliente não encontrado"

def test_widraw_money_client_pf_insufficient_balance():
    controller = WithdrawMoneyController(MockPessoaFisicaRepository(), MockPessoaJuridicaRepository())

    with pytest.raises(Exception) as exc_info:
        controller.withdraw_money(5500,1,"PF")

    assert str(exc_info.value) == "Saldo insuficiente"

def test_widraw_money_client_pf():
    controller = WithdrawMoneyController(MockPessoaFisicaRepository(), MockPessoaJuridicaRepository())

    response = controller.withdraw_money(500,1,"PF")

    expected_response = {
            "data": {
                "type": "Pessoa Fisica",
                "count": 1,
                "attributes": {
                    "amount": 500,
                    "new_balance": 4500
                }
            }
        }
    
    assert response == expected_response

def test_widraw_money_client_pj_not_found():
    controller = WithdrawMoneyController(MockPessoaFisicaNotFoundRepository(), MockPessoaJuridicaNotFoundRepository())

    with pytest.raises(Exception) as exc_info:
        controller.withdraw_money(100,1,"PJ")

    assert str(exc_info.value) == "Cliente não encontrado"

def test_widraw_money_client_pj_insufficient_balance():
    controller = WithdrawMoneyController(MockPessoaFisicaRepository(), MockPessoaJuridicaRepository())

    with pytest.raises(Exception) as exc_info:
        controller.withdraw_money(60000,1,"PJ")

    assert str(exc_info.value) == "Saldo insuficiente"

def test_widraw_money_client_pj():
    controller = WithdrawMoneyController(MockPessoaFisicaRepository(), MockPessoaJuridicaRepository())

    response = controller.withdraw_money(5000,1,"PJ")

    expected_response = {
            "data": {
                "type": "Pessoa Juridica",
                "count": 1,
                "attributes": {
                    "amount": 5000,
                    "new_balance": 45000
                }
            }
        }
    
    assert response == expected_response
