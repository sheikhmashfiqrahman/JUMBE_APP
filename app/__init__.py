# from  flask import Flask
# from .routes import configure_routes

# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address

# def create_app():
#     app = Flask(__name__)
    

#     # Configure Flask-Limiter
#     #limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"])
#     configure_routes(app)
#     return app