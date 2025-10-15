from flask import jsonify
from pymongo import MongoClient

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
			return jsonify(orders)
		except Exception as e:
			return 'Error: an error ecountred in the orderMongo:', 500

	@staticmethod
	def createOrder(body):
		try:
			order = orderMongo.collectionOrder.insert_one(body)
			return	jsonify({"Message": "Order created successfully!", "id":str(order.inserted_id)}) , 201
		except Exception as e:
			return 'Error: an error ecountred in the orderMongo:', 500
