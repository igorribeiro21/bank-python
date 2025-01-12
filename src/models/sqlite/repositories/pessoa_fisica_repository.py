from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import update
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface

class PessoaFisicaRepository(PessoaFisicaRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection


    def create(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str,categoria: str, saldo:float) -> None:
        with self.__db_connection as database:
            try:
                pessoa_fisica = PessoaFisica(
                    renda_mensal=renda_mensal,
                    idade=idade,
                    nome_completo=nome_completo,
                    celular=celular,
                    email=email,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(pessoa_fisica)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
       
    def get(self) -> list[PessoaFisica]:
        with self.__db_connection as database:
            try:
                pessoas_fisica = database.session.query(PessoaFisica).all()

                return pessoas_fisica
            except Exception as exception:
                raise exception
            
    def update_saldo(self, pessoa_fisica_id: int, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                stmt = (
                    update(PessoaFisica)
                    .where(PessoaFisica.id == pessoa_fisica_id)
                    .values(saldo=saldo)
                )

                database.session.execute(stmt)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    def get_pessoa_fisica(self, pessoa_fisica_id: int) -> PessoaFisica:
        with self.__db_connection as database:
            try:
                pessoa_fisica = (
                    database.session
                        .query(PessoaFisica)
                        .filter(PessoaFisica.id == pessoa_fisica_id)                        
                        .one()
                )
                return pessoa_fisica
            except NoResultFound:
                return None
