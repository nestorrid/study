from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:00000000@127.0.0.1:3306/study_flask'

db = SQLAlchemy(app)


api = Api(app)


class User(Resource):

    def get(self, name):
        return {'user': name}


api.add_resource(User, '/user/<string:name>')


@app.route('/')
def index():
    return "hello world!"


@app.route('/arg')
def print_arg():
    id = request.args.get('id', 1)
    return f'request id is {id!r}'
