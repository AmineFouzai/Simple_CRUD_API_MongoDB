
'''
Preset controller by torn for / route
'''
from .modules import *
class homeHandler(tornado.web.RequestHandler):
	"""CRUD CYCLE"""
	#READ
	def get(self):
		client=  user()
		self.write(tornado.escape.json_encode(client.get()))
		self.set_status(200)
		
	#Create
	def post(self):
		record=tornado.escape.json_decode(self.request.body)
		client=user(record['first_name'],record['last_name'],record['date'])
		client.add()
		self.get()

	#DELETE
	def delete(self):
		client=user()
		client.delete(tornado.escape.json_decode(self.request.body)['id'])
		self.get()

	#UPDATE	
	def put(self):
		data=tornado.escape.json_decode(self.request.body)
		client=user(data['first_name'],data['last_name'],data['date'])
		client.update(data['id'])
		self.get()
					