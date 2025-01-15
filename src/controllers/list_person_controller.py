from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from src.controllers.interfaces.list_person_controller import ListPersonControllerInterface

class ListPersonController(ListPersonControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface):
        self.__pessoa_fisica_repository = pessoa_fisica_repository
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def list_person(self, type: str) -> dict:
        formated_response = {}

        if type == "PF":
            list_response = self.__list_pessoa_fisica_in_db()

            formated_response = self.__format_response(list_response, "Pessoa Fisica")
        elif type == "PJ":
            list_response = self.__list_pessoa_juridica_in_db()

            formated_response = self.__format_response(list_response, "Pessoa Juridica")
        else:
            raise Exception("Tipo informado é inválido!")
        
        return formated_response


    def __list_pessoa_fisica_in_db(self) -> list[PessoaFisica]:
        list_pessoa_fisica = self.__pessoa_fisica_repository.get()

        return list_pessoa_fisica
    
    def __list_pessoa_juridica_in_db(self) -> list[PessoaJuridica]:
        list_pessoa_juridica = self.__pessoa_juridica_repository.get()

        return list_pessoa_juridica
    
    def __format_response(self, list: list[PessoaFisica] | list[PessoaJuridica], type: str) -> dict:
        return {
            "data": {
                "type": type,
                "count": len(list),
                "attributes":list
            }
        }
