from abc import ABC,abstractmethod
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica

class PessoaJuridicaRepositoryInterface(ABC):

    @abstractmethod
    def create(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str,categoria: str, saldo:float) -> None:
        pass

    @abstractmethod
    def get(self) -> list[PessoaJuridica]:
        pass

    @abstractmethod
    def update_saldo(self, pessoa_juridica_id: int, faturamento: float) -> None:
        pass

    @abstractmethod
    def get_pessoa_juridica(self, pessoa_juridica_id: int) -> PessoaJuridica:
        pass