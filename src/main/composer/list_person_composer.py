from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.list_person_controller import ListPersonController
from src.views.list_person_view import ListPersonView

def list_person_composer():
    pessoa_fisica_repository = PessoaFisicaRepository(db_connection_handler)
    pessoa_juridica_repository = PessoaJuridicaRepository(db_connection_handler)
    controller = ListPersonController(pessoa_fisica_repository, pessoa_juridica_repository)
    view = ListPersonView(controller)

    return view
