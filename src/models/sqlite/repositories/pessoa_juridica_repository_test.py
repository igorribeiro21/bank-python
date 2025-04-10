from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from .pessoa_juridica_repository import PessoaJuridicaRepository

class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()

        query_mock = mock.Mock()
        query_mock.all.return_value = [
            PessoaJuridica(
                faturamento=1500.00,
                idade=30,
                nome_fantasia="Jhon Doe",
                celular="99653-6596",
                email_corporativo="teste@teste.com",
                categoria="Categoria A",
                saldo=8000.00,
            )
        ]
        self.session.query.return_value = query_mock

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNoResult:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()
        self.session.add.side_effect = self.__raise_no_result_found
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_create():
    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)

    faturamento=1200.00
    idade=35
    nome_fantasia="João Silva"
    celular="99653-7895"
    email_corporativo="teste@teste.com"
    categoria="Categoria A"
    saldo=5000.00

    repo.create(faturamento,idade,nome_fantasia,celular,email_corporativo,categoria,saldo)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_create_exception():
    mock_connection = MockConnection()
    mock_connection.session.add.side_effect = Exception("Erro ao adicionar no banco de dados")
    repo = PessoaJuridicaRepository(mock_connection)

    faturamento = 1200.00
    idade = 35
    nome_fantasia = "João Silva"
    celular = "99653-7895"
    email_corporativo = "teste@teste.com"
    categoria = "Categoria A"
    saldo = 5000.00

    with pytest.raises(Exception, match="Erro ao adicionar no banco de dados"):
        repo.create(faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)

    mock_connection.session.rollback.assert_called_once()
    mock_connection.session.commit.assert_not_called()

def test_get():
    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)

    response = repo.get()

    mock_connection.session.query.assert_called_once_with(PessoaJuridica)
    assert len(response) == 1
    assert isinstance(response[0], PessoaJuridica)
    assert response[0].nome_fantasia == "Jhon Doe"
    assert response[0].idade == 30
    assert response[0].faturamento == 1500.00
    assert response[0].categoria == "Categoria A"
    assert response[0].email_corporativo == "teste@teste.com"

def test_get_exception():
    mock_connection = MockConnection()
    mock_connection.session.query.side_effect = Exception("Erro no banco de dados")

    repo = PessoaJuridicaRepository(mock_connection)

    with pytest.raises(Exception) as exc_info:
        repo.get()

    assert str(exc_info.value) == "Erro no banco de dados"

    mock_connection.session.query.assert_called_once_with(PessoaJuridica)

def test_update_faturamento():
    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)

    pessoa_juridica_id = 1
    novo_saldo = 10000.00

    repo.update_saldo(pessoa_juridica_id, novo_saldo)

    mock_connection.session.execute.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_update_faturamento_exception():
    mock_connection = MockConnection()
    mock_connection.session.execute.side_effect = Exception("Erro ao atualizar saldo")

    repo = PessoaJuridicaRepository(mock_connection)

    pessoa_juridica_id = 1
    novo_saldo = 10000.00

    with pytest.raises(Exception, match="Erro ao atualizar saldo"):
        repo.update_saldo(pessoa_juridica_id, novo_saldo)

    mock_connection.session.rollback.assert_called_once()
    mock_connection.session.commit.assert_not_called()

def test_get_pessoa_juridica():
    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)

    repo.get_pessoa_juridica(1)

    mock_connection.session.query.assert_called_once_with(PessoaJuridica)

def test_get_pessoa_juridica_error():
    mock_connection = MockConnectionNoResult()
    repo = PessoaJuridicaRepository(mock_connection)

    response = repo.get_pessoa_juridica(1)

    assert response is None
