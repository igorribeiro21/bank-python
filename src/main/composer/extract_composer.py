from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.extract_controller import ExtractController
from src.views.extract_view import ExtractView

def extract_composer():
    pessoa_fisica_repository = PessoaFisicaRepository(db_connection_handler)
    pessoa_juridica_repository = PessoaJuridicaRepository(db_connection_handler)
    controller = ExtractController(pessoa_fisica_repository, pessoa_juridica_repository)
    view = ExtractView(controller)

    return view
