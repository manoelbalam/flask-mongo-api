from flask import jsonify
from dbaccess.orderDBA import orderMongo
from bson import ObjectId
import pdb


class orderLogic():
  @staticmethod
  def listOrders():
    # Basic Logic
    try:
      return orderMongo.listOrders()
    except Exception as e:
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def createOrder(body):
    # Basic Logic
    # pdb.set_trace()
    try:
      if 'customer_name' not in body:
        return  jsonify({"error": "customer_name field is mandatory"}) , 404
      body['status'] = 'inProgress'
      return orderMongo.createOrder(body)
    except Exception as e:
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def getOrderByID(order_id):
    # Basic Logic
    try:
      if ObjectId(order_id):
        return orderMongo.getOrderByID(order_id)
    except Exception as e:
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def updateOrderByID(order_id, body):
    # Basic Logic
    try:
      if 'status' not in body:
        return  jsonify({"error": "status field is mandatory"}) , 400
      # if ObjectId(order_id):
      return orderMongo.updateOrderByID(order_id, body)
    except Exception as e:
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def deleteOrderByID(order_id):
    # Basic Logic
    try:
      if ObjectId(order_id):
        return orderMongo.deleteOrderByID(order_id)
    except Exception as e:
      return jsonify({"Error": str(e)}), 500