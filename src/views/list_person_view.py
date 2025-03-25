
from src.controllers.interfaces.list_person_controller import ListPersonControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class ListPersonView(ViewInterface):
    def __init__(self, controller: ListPersonControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        type = http_request.param["type"]

        body_response = self.__controller.list_person(type)

        return HttpResponse(status_code=200, body=body_response)
