from flask import jsonify
from dbaccess.orderDBA import orderMongo

class orderLogic():
	@staticmethod
	def listOrders():
		# Basic Logic
		try:
			return orderMongo.listOrders()
		except Exception as e:
			return 'Error:orderLogic:listOrders:', 500

	@staticmethod
	def createOrder(body):
		# Basic Logic
		try:
			if 'customer_name' not in body:
			  return  jsonify({"error": "customer_name field is mandatory"}) , 400
			return orderMongo.createOrder(body)
		except Exception as e:
			return 'Error:orderLogic:createOrder:', 500