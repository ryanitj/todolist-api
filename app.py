from flask import Flask
from api.routes.task import task_blueprint
from flask import Flask, jsonify
from flask_swagger import swagger
from flask_smorest import Api
from database.db import db
from flask_migrate import Migrate
from config.env import DB_NAME, DB_PORT, DB_URL 

def init_app():
    app = Flask(__name__)
    migrate = Migrate()

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f"{DB_URL}:{DB_PORT}/{DB_NAME}" 
    app.config["API_TITLE"] = "TodoList REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/api/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    
    api = Api(app=app)
    api.register_blueprint(task_blueprint)
    
    db.init_app(app)
    migrate.init_app(app, db)
     
    return app


app = init_app()

if __name__ == "__main__":
    app.run()
    

