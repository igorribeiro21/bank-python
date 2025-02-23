from abc import abstractmethod,ABC

class WithdrawMoneyControllerInterface(ABC):

    @abstractmethod
    def withdraw_money(self,amount: float,client_id:int, type_person: str) -> dict:
        pass
