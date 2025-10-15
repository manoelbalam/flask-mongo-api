from flask import Flask, jsonify, request
from controllers.orderController import orderBP
from flasgger import Swagger

# import pdb
app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'flask-mongo-api',
    'description': 'API RESTful CRUD Orders',
    'version': 'v0.1',
    'uiversion': 2
}

swagger = Swagger(app)

app.register_blueprint(orderBP)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)