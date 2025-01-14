from abc import abstractmethod, ABC

class CreatePersonControllerInterface(ABC):

    @abstractmethod
    def create(self, person_info: dict) -> dict:
        pass
