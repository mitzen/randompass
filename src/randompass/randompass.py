from flask import request, jsonify, redirect
from flask_restx import Resource
import string
import secrets

class SimplePassword(Resource):

    def get(self, passwordLength: int = 20):
        pwdgenerator = RandomPasswordGenerator().generate_password(passwordLength)
        return jsonify(pwdgenerator)

class RandomPasswordGenerator:
    def __init__(self) -> None:
        pass

    def generate_password(self, passwordLength : int = 20) -> str:
        return ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(passwordLength))