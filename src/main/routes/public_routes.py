from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.withdraw_money_composer import withdraw_money_composer

from src.errors.error_handler import handle_errors

public_route_bp = Blueprint("public_routes", __name__)

@public_route_bp.route("/withdraw/<client_id>/<type>", methods=["PUT"])
def withdraw_money(client_id, type):
    try:
        http_request = HttpRequest(body=request.json, param={ "client_id": client_id, "type": type })
        view = withdraw_money_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
