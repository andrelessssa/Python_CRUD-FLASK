from routes import api
from __init__ import create_app

app = create_app()
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
