import re
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from src.controllers.interfaces.create_person_controller import CreatePersonControllerInterface

class CreatePersonController(CreatePersonControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface):
        self.__pessoa_fisica_repository = pessoa_fisica_repository
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def create(self, person_info: dict) -> dict:
        formated_response = {}

        if person_info["type"] == "PF":
            renda_mensal = person_info["renda_mensal"]
            idade = person_info["idade"]
            nome_completo = person_info["nome_completo"]
            celular = person_info["celular"]
            email = person_info["email"]
            categoria = person_info["categoria"]
            saldo = person_info["saldo"]

            self.__validate_name(nome_completo)
            self.__insert_pessoa_fisica_in_db(renda_mensal,idade,nome_completo,celular,email,categoria,saldo)

            del person_info["type"]

            formated_response = self.__format_response(person_info, "Pessoa Fisica")
        elif person_info["type"] == "PJ":
            faturamento = person_info["faturamento"]
            idade = person_info["idade"]
            nome_fantasia = person_info["nome_fantasia"]
            celular = person_info["celular"]
            email_corporativo = person_info["email_corporativo"]
            categoria = person_info["categoria"]
            saldo = person_info["saldo"]

            self.__validate_name(nome_fantasia)
            self.__insert_pessoa_juridica_in_db(faturamento,idade,nome_fantasia,celular,email_corporativo,categoria,saldo)

            del person_info["type"]

            formated_response = self.__format_response(person_info, "Pessoa Fisica")
        else:
            raise Exception("Tipo informado é inválido!")

        return formated_response


    def __insert_pessoa_fisica_in_db(self,renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str,categoria: str, saldo:float) -> None:
        self.__pessoa_fisica_repository.create(renda_mensal,idade,nome_completo,celular,email,categoria,saldo)

    def __insert_pessoa_juridica_in_db(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str,categoria: str, saldo:float) -> None:
        self.__pessoa_juridica_repository.create(faturamento,idade,nome_fantasia,celular,email_corporativo,categoria,saldo)

    def __validate_name(self, name: str) -> None:
        # Expressão Regular para caracteres que não são letras
        non_valid_caracteres = re.compile(r'[^a-zA-Z ]')

        if non_valid_caracteres.search(name):
            raise Exception ("Nome da pessoa inválido!")

    def __format_response(self, person_info: dict, tipo: str) -> dict:
        return {
            "data": {
                "type": tipo,
                "count": 1,
                "attributes": person_info
            }
        }
