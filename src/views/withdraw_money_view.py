from src.controllers.interfaces.withdraw_money_controller import WithdrawMoneyControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class WithdrawMoneyView(ViewInterface):
    def __init__(self, controller: WithdrawMoneyControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        client_id = http_request.param["client_id"]
        type = http_request.param["type"]
        amount = http_request.body["amount"]

        body_response = self.__controller.withdraw_money(amount, client_id, type)

        return HttpResponse(status_code=200, body=body_response)
