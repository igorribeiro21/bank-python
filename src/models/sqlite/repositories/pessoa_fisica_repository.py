from src.models.sqlite.entities.pessoa_fisica import PessoaFisica

class PessoaFisicaRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection


    def create(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str,categoria: str, saldo:float) -> None:
        with self.__db_connection as database:
            try:
                pessoa_fisica = PessoaFisica(
                    renda_mensal,
                    idade,
                    nome_completo,
                    celular,
                    email,
                    categoria,
                    saldo
                )
                database.session.add(pessoa_fisica)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    def get(self) -> list[PessoaFisica]:
        with self.__db_connection as database:
            try:
                pessoas_fisica = (
                    database.session
                        .query(PessoaFisica)
                        .all()
                )
                return pessoas_fisica
            except Exception as exception:
                raise exception
