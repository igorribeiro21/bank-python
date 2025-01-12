from abc import ABC,abstractmethod
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica

class PessoaFisicaRepositoryInterface(ABC):

    @abstractmethod
    def create(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str,categoria: str, saldo:float) -> None:
        pass

    @abstractmethod
    def get(self) -> list[PessoaFisica]:
        pass

    @abstractmethod
    def update_saldo(self, pessoa_fisica_id: int, saldo: float) -> None:
        pass

    @abstractmethod
    def get_pessoa_fisica(self, pessoa_fisica_id: int) -> PessoaFisica:
        pass