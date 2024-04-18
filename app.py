
from  flask import Flask
import os
from app.routes import configure_routes
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Entry point of the application
app = Flask(__name__)

configure_routes(app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    