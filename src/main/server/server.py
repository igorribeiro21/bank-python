from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler

from src.main.routes.admin_routes import admin_route_bp
from src.main.routes.public_routes import public_route_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(admin_route_bp)
app.register_blueprint(public_route_bp)
