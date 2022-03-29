from flask import Flask
from flask_cors import CORS


def create_app():
    # arg config_filename => aqui el env
    
    app = Flask(__name__)
    CORS(app)
    
    # app.config.from_pyfile(config_filename)

    from repository import db_atlas
    
    db_atlas.init_app(app)

    return app