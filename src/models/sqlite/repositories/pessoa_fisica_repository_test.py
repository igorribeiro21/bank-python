from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from .pessoa_fisica_repository import PessoaFisicaRepository

class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.add(PessoaFisica), mock.call.query(PessoaFisica)], #query
                    [
                        PessoaFisica(renda_mensal=1500.00,idade=30,nome_completo="Jhon Doe",celular="99653-6596",email="teste@teste.com",categoria="Categoria A",saldo=8000.00)
                    ] #resultado
                )
            ]
        )

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_create():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)

    renda_mensal=1200.00
    idade=35
    nome_completo="João Silva"
    celular="99653-7895"
    email="teste@teste.com"
    categoria="Categoria A"
    saldo=5000.00

    repo.create(renda_mensal,idade,nome_completo,celular,email,categoria,saldo)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_create_exception():
    mock_connection = MockConnection()
    mock_connection.session.add.side_effect = Exception("Erro ao adicionar no banco de dados")
    repo = PessoaFisicaRepository(mock_connection)

    renda_mensal = 1200.00
    idade = 35
    nome_completo = "João Silva"
    celular = "99653-7895"
    email = "teste@teste.com"
    categoria = "Categoria A"
    saldo = 5000.00

    with pytest.raises(Exception, match="Erro ao adicionar no banco de dados"):
        repo.create(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)

    mock_connection.session.rollback.assert_called_once()
    mock_connection.session.commit.assert_not_called()
