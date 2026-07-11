from flask import Flask
from config import SECRET_KEY, DEBUG
from routes import register_routes

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY
app.config["DEBUG"] = DEBUG

# Register all routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=DEBUG)