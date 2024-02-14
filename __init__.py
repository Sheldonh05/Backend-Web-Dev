from flask import Flask
### to create an app on flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Sheldon code'

    from views import views
    from auth import auth
### establishes the prefix in the url
    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix="/")

    return app

app = create_app()

### debugs code after changes
if __name__ == '__main__':
    app.run(debug=True)
