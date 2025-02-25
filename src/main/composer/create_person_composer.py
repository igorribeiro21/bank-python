from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.create_person_controller import CreatePersonController
from src.views.create_person_view import CreatePersonView

def create_person_composer():
    pessoa_fisica_repository = PessoaFisicaRepository(db_connection_handler)
    pessoa_juridica_repository = PessoaJuridicaRepository(db_connection_handler)
    controller = CreatePersonController(pessoa_fisica_repository, pessoa_juridica_repository)
    view = CreatePersonView(controller)

    return view
