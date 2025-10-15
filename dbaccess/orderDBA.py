from flask import jsonify
from pymongo import MongoClient
import pdb
class orderMongo:

	client = MongoClient('mongodb://127.0.0.1:27017/')
	db = client['flask-mongo-api']
	collectionOrder = db['order']

	@staticmethod
	def listOrders():
		# pdb.set_trace()s
		try:
			order = list(orderMongo.collectionOrder.find())
			return jsonify(order)
		except Exception as e:
			return 'Error: an error ecountred in the orderMongo:', 500