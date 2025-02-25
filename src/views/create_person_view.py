from src.controllers.interfaces.create_person_controller import CreatePersonControllerInterface
from src.validators.create_person_pf_validator import create_person_pf_validator
from src.validators.create_person_pj_validator import create_person_pj_validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class CreatePersonView(ViewInterface):

    def __init__(self, controller: CreatePersonControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        if http_request.body["type"] is None:
            raise HttpUnprocessableEntityError("Tipo de pessoa não foi informado!")

        if http_request.body["type"] == "PF":
            create_person_pf_validator(http_request)
        else:
            create_person_pj_validator(http_request)

        person_info = http_request.body

        body_response = self.__controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response)
