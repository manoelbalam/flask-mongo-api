from flask import Blueprint, jsonify, request
from logic.orderLogic import orderLogic
import pdb
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
      - name: status
        in: query
        description: 'Type of user to filter'
        required: true
        type: string
        enum:
          - inProgress
          - Done
          - Delivered

      - in: body
        name: body
        description: 'Specting a object like: {"customer_name" : "customer_name" }'
        schema:
          $ref: 'Object'
    responses:
      201:
        description: The Order has been created
        schema:
          type: array
          items:
            type: object
            properties:
              Message:
                type: string
              id:
                type: string
    """
	try:
		body = request.get_json()
		return orderLogic.createOrder(body)
	except Exception as e:
		return jsonify({"Error": str(e)}), 500

@orderBP.route("/api/orders/<string:order_id>", methods = ["GET"])
def getOrderByID(order_id):
  """
  Retrieve order by Id
  ---
    tags:
      - Orders
    parameters:
      - in: path
        name: order_id
        required: true
        description: The ID of the order, must be a valid!
        type: string
    responses:
      201:
        description: The task has been updated
        schema:
          type: array
          items:
            type: object
            properties:
              Message:
                type: string
              id:
                type: string
    """
  try:
    return orderLogic.getOrderByID(order_id)
  except Exception as e:
    return jsonify({"Error": str(e)}), 500

@orderBP.route("/api/orders/<string:order_id>", methods = ["PATCH"])
def updateOrderByID(order_id):
  """
      patch endpoint
      ---      
      tags:
        - Orders
      parameters:
        - name: a
          in: query
          type: integer
          required: true
          description: first number
        - name: b
          in: query
          type: integer
          required: true
          description: second number
      responses:
        500:
          description: Error The number is not integer!
        200:
          description: Number statistics
          schema:
            id: stats
            properties:
              sum:
                type: integer
                description: The sum of number
              product:
                type: integer
                description: The sum of number
              division:
                type: integer
                description: The sum of number              
      """
  try:
    body = request.get_json()
    return orderLogic.updateOrderByID(order_id, body)
  except Exception as e:
    return jsonify({"Error": str(e)}), 500

@orderBP.route("/api/orders/<string:order_id>", methods = ["DELETE"])
def deleteOrderByID(order_id):
  """
  Delete order by Id
  ---
  tags:
    - Orders
  parameters:
    - in: path
      name: order_id
      required: true
      description: The ID of the order, must be a valid!
      type: string
  responses:
    201:
      description: The task has been updated
      schema:
        $ref: '#/definitions/Task'
  """
  try:
    return orderLogic.deleteOrderByID(order_id)
  except Exception as e:
    return jsonify({"Error": str(e)}), 500