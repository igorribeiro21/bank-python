from src.controllers.interfaces.extract_controller import ExtractControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class ExtractView(ViewInterface):

    def __init__(self, controller: ExtractControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        client_id = http_request.param["client_id"]
        type = http_request.param["type"]

        body_response = self.__controller.extract(client_id, type)

        return HttpResponse(status_code=200, body=body_response)
