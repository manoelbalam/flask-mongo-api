from flask import jsonify
from pymongo import MongoClient
import pdb

from bson import ObjectId

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
      return jsonify(orders), 200
    except Exception as e:
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def createOrder(body):
    try:
      order = orderMongo.collectionOrder.insert_one(body)
      return  jsonify({"Message": "Order created successfully!", "id":str(order.inserted_id)}) , 201
    except Exception as e:
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def getOrderByID(order_id):    
    try:
      order = orderMongo.collectionOrder.find_one({"_id": ObjectId(order_id)})
      if order:
        order['_id'] = str(order['_id'])
        return jsonify(order), 200
      return jsonify({"Error": "Order not found"}), 404
    except Exception as e:
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def updateOrderByID(order_id, body):  
    try:
      # data = request.json
      updated_data = {"$set": {"customer_name": body.get("customer_name"), "status": body.get("status")}}

      order = orderMongo.collectionOrder.update_one({"_id": ObjectId(order_id)}, updated_data)

      if order.matched_count:
          updated_order = orderMongo.collectionOrder.find_one({"_id": ObjectId(order_id)})
          updated_order['_id'] = str(updated_order['_id'])
          return jsonify(updated_order), 200
      return jsonify({"error": "Order not found"}), 404
    except Exception as e:
      return jsonify({"Error": str(e)}), 500

  @staticmethod
  def deleteOrderByID(order_id):  
    # pdb.set_trace()  
    try:
      order = orderMongo.collectionOrder.delete_one({"_id": ObjectId(order_id)})

      if order.deleted_count:
        return jsonify({"Message": "Order deleted successfully"})
      return jsonify({"Error": "Order not found"}), 404
    except Exception as e:
      return jsonify({"Error": str(e)}), 500