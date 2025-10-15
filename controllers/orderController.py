from flask import Blueprint, jsonify, request
from logic.orderLogic import orderLogic

orderBP = Blueprint('orders', __name__)

@orderBP.route("/api/orders/", methods = ["GET"])
def listOrders():
	"""
    Retrieve Orders.
    ---
    tags:
      - Orders
    responses:
      200:
        description: A list of orders.
        schema:
          type: array
          items:
            type: object
            properties:
              _id:
                type: string
              customer_name:
                type: string
    """
	try:
		return orderLogic.listOrders()
	except Exception as e:
		return 'Error:orderController:listOrders', 500

@orderBP.route("/api/orders/", methods = ["POST"])
def createOrder():
	"""
    Create Order
    ---
    tags:
      - Orders
    parameters:
      - in: body
        name: body
        description: 'Specting a object like: {"customer_name" : "test" }'
        schema:
          $ref: '#/definitions/Order'
    responses:
      201:
        description: The Order has been created
        schema:
          $ref: '#/definitions/Order'
    """
	try:
		body = request.get_json()
		return orderLogic.createOrder(body)
	except Exception as e:
		return 'Error:orderController:createOrder', 500
