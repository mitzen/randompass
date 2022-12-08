from flask import Flask
from flask_restx import Api
from randompass import SimplePassword

app = Flask(__name__)
api = Api(app)
api.add_resource(SimplePassword, '/password/<int:passwordLength>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')