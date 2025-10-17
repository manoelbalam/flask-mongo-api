from bson import ObjectId
from flask import jsonify
from pymongo import MongoClient
import logging
import pdb

error_log = logging.getLogger("error_log")
info_log = logging.getLogger("info_log")

class orderMongo:

  client = MongoClient('mongodb://127.0.0.1:27017/')
  db = client['flask-mongo-api']
  collectionOrder = db['order']

  @staticmethod
  def listOrders():
    try:
      orders = list(orderMongo.collectionOrder.find())
      for order in orders:
        order['_id'] = str(order['_id'])
      info_log.info(f'orders retrieved:{len(orders)}')
      return jsonify(orders), 200
    except Exception as e:
      error_log.error(str(e))
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def createOrder(body):
    try:
      order = orderMongo.collectionOrder.insert_one(body)
      info_log.info(f'order _id:{order_id} created')
      return  jsonify({"Message": "Order created successfully!", "id":str(order.inserted_id)}) , 201
    except Exception as e:
      error_log.error(str(e))
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def getOrderByID(order_id):    
    try:
      order = orderMongo.collectionOrder.find_one({"_id": ObjectId(order_id)})
      if order:
        order['_id'] = str(order['_id'])
        info_log.info(f'order _id:{order_id} retrieved')
        return jsonify(order), 200
      info_log.info(f'order _id:{order_id} not found')
      return jsonify({"Error": "Order not found"}), 404
    except Exception as e:
      error_log.error(str(e))
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def updateOrderByID(order_id, body):  
    try:
      updated_data = {"$set": {"customer_name": body.get("customer_name"), "status": body.get("status")}}
      order = orderMongo.collectionOrder.update_one({"_id": ObjectId(order_id)}, updated_data)
      if order.matched_count:
          updated_order = orderMongo.collectionOrder.find_one({"_id": ObjectId(order_id)})
          updated_order['_id'] = str(updated_order['_id'])
          info_log.info(f'order _id:{order_id} updated')
          return jsonify(updated_order), 200
      info_log.info(f'order _id:{order_id} not found')
      return jsonify({"error": "Order not found"}), 404
    except Exception as e:
      error_log.error(str(e))
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def deleteOrderByID(order_id):  
    try:
      order = orderMongo.collectionOrder.delete_one({"_id": ObjectId(order_id)})
      if order.deleted_count:
        info_log.info(f'order _id:{order_id} deleted')
        return jsonify({"Message": "Order deleted successfully"})
      info_log.info(f'order _id:{order_id} not found')
      return jsonify({"Error": "Order not found"}), 404
    except Exception as e:
      error_log.error(str(e))
      return jsonify({"Error": str(e)}), 500