from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface

class WithdrawMoneyController:

    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface):
        self.__pessoa_fisica_repository = pessoa_fisica_repository
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def withdraw_money(self,amount: float,client_id:int, type_person: str):
        amount_client = 0.00
        new_balance = 0.00
        format_response = {}

        if type_person == "PF":
            client = self.__get_pessoa_fisica_in_db(client_id)

            amount_client = float(client["saldo"])
            if amount > amount_client:
                raise Exception("Saldo insuficiente")

            new_balance = amount_client - amount

            self.__pessoa_fisica_repository.update_saldo(client_id, new_balance)

            format_response = self.__format_response(amount, new_balance, "Pessoa Fisica")

        elif type_person == "PJ":
            client = self.__get_pessoa_juridica_in_db(client_id)

            amount_client = float(client["saldo"])

            if amount > amount_client:
                raise Exception("Saldo insuficiente")

            new_balance = amount_client - amount

            self.__pessoa_juridica_repository.update_faturamento(client_id, new_balance)

            format_response = self.__format_response(amount, new_balance, "Pessoa Juridica")

        return format_response

    def __get_pessoa_fisica_in_db(self,pessoa_fisica_id) -> PessoaFisica:
        client = self.__pessoa_fisica_repository.get_pessoa_fisica(pessoa_fisica_id)

        if client is None:
            raise Exception("Cliente não encontrado")

        return client

    def __get_pessoa_juridica_in_db(self,pessoa_juridica_id) -> PessoaJuridica:
        client = self.__pessoa_juridica_repository.get_pessoa_juridica(pessoa_juridica_id)

        if client is None:
            raise Exception("Cliente não encontrado")

        return client

    def __format_response(self, amount: float, new_balance: float, type_person: str) -> dict:
        return {
            "data": {
                "type": type_person,
                "count": 1,
                "attributes": {
                    "amount": amount,
                    "new_balance": new_balance
                }
            }
        }
