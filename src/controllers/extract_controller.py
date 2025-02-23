from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from src.controllers.interfaces.extract_controller import ExtractControllerInterface

class ExtractController(ExtractControllerInterface):

    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface):
        self.__pessoa_fisica_repository = pessoa_fisica_repository
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def extract(self,client_id:int, type_person: str) -> dict:
        format_response = {}

        if type_person == "PF":
            client = self.__get_pessoa_fisica_in_db(client_id)

            format_response = self.__format_response(client["nome_completo"], client["saldo"], "Pessoa Fisica")

        elif type_person == "PJ":
            client = self.__get_pessoa_juridica_in_db(client_id)

            format_response = self.__format_response(client["nome_fantasia"], client["saldo"], "Pessoa Juridica")

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

    def __format_response(self, name: str, balance: float, type_person: str) -> dict:
        return {
            "data": {
                "type": type_person,
                "count": 1,
                "attributes": {
                    "name": name,
                    "balance": balance,
                    "type": type_person
                }
            }
        }
