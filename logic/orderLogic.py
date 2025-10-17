from flask import jsonify
from dbaccess.orderDBA import orderMongo
from bson import ObjectId
import logging

error_log = logging.getLogger("error_log")
info_log = logging.getLogger("info_log")

class orderLogic():
  @staticmethod
  def listOrders():
    # Basic Logic
    try:
      return orderMongo.listOrders()
    except Exception as e:
      error_log.error(str(e))
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def createOrder(body):
    # Basic Logic
    try:
      if 'customer_name' not in body:
        return  jsonify({"error": "customer_name field is mandatory"}) , 404
      body['status'] = 'inProgress'
      info_log.info(f'create order logic success')
      return orderMongo.createOrder(body)
    except Exception as e:
      error_log.error(str(e))
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def getOrderByID(order_id):
    # Basic Logic
    try:
      if ObjectId(order_id):
        info_log.info(f'get order logic success')
        return orderMongo.getOrderByID(order_id)
    except Exception as e:
      error_log.error(str(e))
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def updateOrderByID(order_id, body):
    # Basic Logic
    try:
      if 'status' not in body:
        return  jsonify({"error": "status field is mandatory"}) , 400
      info_log.info(f'create order logic success')
      return orderMongo.updateOrderByID(order_id, body)
    except Exception as e:
      error_log.error(str(e))
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def deleteOrderByID(order_id):
    # Basic Logic
    try:
      if ObjectId(order_id):
        info_log.info(f'delete order logic success')
        return orderMongo.deleteOrderByID(order_id)
    except Exception as e:
      error_log.error(str(e))
      return jsonify({"Error": str(e)}), 500