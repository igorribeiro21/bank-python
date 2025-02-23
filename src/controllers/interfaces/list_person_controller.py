from abc import abstractmethod,ABC

class ListPersonControllerInterface(ABC):

    @abstractmethod
    def list_person(self, type: str) -> dict:
        pass