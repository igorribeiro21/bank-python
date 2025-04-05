from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.withdraw_money_controller import WithdrawMoneyController
from src.views.withdraw_money_view import WithdrawMoneyView

def withdraw_money_composer():
    pessoa_fisica_repository = PessoaFisicaRepository(db_connection_handler)
    pessoa_juridica_repository = PessoaJuridicaRepository(db_connection_handler)
    controller = WithdrawMoneyController(pessoa_fisica_repository, pessoa_juridica_repository)
    view = WithdrawMoneyView(controller)

    return view
