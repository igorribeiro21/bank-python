from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import update
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface

class PessoaJuridicaRepository(PessoaJuridicaRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection


    def create(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str,categoria: str, saldo:float) -> None:
        with self.__db_connection as database:
            try:
                pessoa_juridica = PessoaJuridica(
                    faturamento=faturamento,
                    idade=idade,
                    nome_fantasia=nome_fantasia,
                    celular=celular,
                    email_corporativo=email_corporativo,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(pessoa_juridica)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
       
    def get(self) -> list[PessoaJuridica]:
        with self.__db_connection as database:
            try:
                pessoas_fisica = database.session.query(PessoaJuridica).all()

                return pessoas_fisica
            except Exception as exception:
                raise exception
            
    def update_faturamento(self, pessoa_juridica_id: int, faturamento: float) -> None:
        with self.__db_connection as database:
            try:
                stmt = (
                    update(PessoaJuridica)
                    .where(PessoaJuridica.id == pessoa_juridica_id)
                    .values(faturamento=faturamento)
                )

                database.session.execute(stmt)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    def get_pessoa_juridica(self, pessoa_juridica_id: int) -> PessoaJuridica:
        with self.__db_connection as database:
            try:
                pessoa_juridica = (
                    database.session
                        .query(PessoaJuridica)
                        .filter(PessoaJuridica.id == pessoa_juridica_id)                        
                        .one()
                )
                return pessoa_juridica
            except NoResultFound:
                return None
