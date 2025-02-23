from abc import abstractmethod,ABC

class ExtractControllerInterface(ABC):

    @abstractmethod
    def extract(self,client_id:int, type_person: str) -> dict:
        pass
