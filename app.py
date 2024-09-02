from flask import Flask as WebApp, render_template as render, request as req, session as sess
from common.database import DatabaseHandler
from models.users.user import UserModel

app_instance = WebApp(__name__)
app_instance.config.from_object('configurations')
app_instance.secret_key = "secure_key_456"

@app_instance.before_request
def setup_database():
    if not hasattr(app_instance, 'database_ready'):
        DatabaseHandler.initialize()
        app_instance.database_ready = True

@app_instance.route('/')
def main_page():
    return render("home.html")

from models.users.views import user_routes
from models.hotels.views import hotel_routes
from models.airlines.views import airline_routes
from models.flights.views import flight_routes
app_instance.register_blueprint(user_routes, url_prefix="/accounts")
app_instance.register_blueprint(hotel_routes, url_prefix="/accommodations")
app_instance.register_blueprint(flight_routes, url_prefix="/journeys")
app_instance.register_blueprint(airline_routes, url_prefix="/carriers")
