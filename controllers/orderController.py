from flask import Blueprint, jsonify, request
from logic.orderLogic import orderLogic

orderBP = Blueprint('orders', __name__)

@orderBP.route("/api/orders/", methods = ["GET"])
def listOrders():
	try:
		return orderLogic.listOrders()
	except Exception as e:
		return 'Error:orderController:listOrders', 500

@orderBP.route("/api/orders/", methods = ["POST"])
def createOrder():
	try:
		body = request.get_json()
		return orderLogic.createOrder(body)
	except Exception as e:
		return 'Error:orderController:createOrder', 500
