from flask import Flask, jsonify, request
from controllers.orderController import orderBP
import pdb
app = Flask(__name__)

app.register_blueprint(orderBP)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)