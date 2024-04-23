from flask import Flask

def createApp():
    app = Flask(__name__)
    app.secret_key = "key" #key to encrypt connection
    # app.config[ "SECRET KEY"] = ?
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    return app
