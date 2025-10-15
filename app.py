from flask import Flask, jsonify, request
from controllers.orderController import orderBP
import pdb
app = Flask(__name__)

app.register_blueprint(orderBP)

if __name__ == '__main__':
    app.run(debug=True)