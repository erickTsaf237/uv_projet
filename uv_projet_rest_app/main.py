from flask import Flask
from flask_restful import Api, Resource, reqparse
from my_resource import ApplicationResource, ParticipantResource
from my_model import db
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///application.db'
db.init_app(app)

with app.app_context():
    db.create_all()
#db.create_all()

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(ApplicationResource, '/applications', '/applications/<int:application_id>')
api.add_resource(ParticipantResource, '/keys', '/keys/<string:user_name>/')



if __name__ == '__main__':
    app.run(debug=True, port=8000)