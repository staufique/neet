from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
def create_app(): 
    username='postgres'
    password='123456'
    host='@localhost'
    port=5432   
    global app
    app=Flask(__name__)

    app.config['SECRET_KEY']='mccramaf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}{host}:{port}/NEET'

    db.init_app(app)

    from app.md.controllers import md_blueprint
    
    app.register_blueprint(
        md_blueprint,
        url_prefix=f'/api{md_blueprint.url_prefix}',
    )

    return app