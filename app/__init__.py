from flask import Flask
from app.extensions import db
#scripts
from app.scripts.create_users import create_users

def create_app():

    #create app instance
    app = Flask(__name__)

    #set config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'key'

    #initialize db
    db.init_app(app)

    #create tables
    with app.app_context():
        db.create_all()
        create_users()

    #import blueprints
    from app.routers.main import main
    from app.routers.user import user

    #register blueprints
    app.register_blueprint(main)
    app.register_blueprint(user)

    #return app instance
    return app