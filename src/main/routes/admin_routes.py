from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.create_person_composer import create_person_composer
from src.main.composer.list_person_composer import list_person_composer

from src.errors.error_handler import handle_errors

admin_route_bp = Blueprint("admin_routes", __name__)

@admin_route_bp.route("/admin/people", methods=["POST"])
def create_person():
    try:
        http_request = HttpRequest(body=request.json)
        view = create_person_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
    
@admin_route_bp.route("/admin/people/<type>",methods=["GET"])
def list_person(type):
    try:
        http_request = HttpRequest(param={ "type": type })
        view = list_person_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
