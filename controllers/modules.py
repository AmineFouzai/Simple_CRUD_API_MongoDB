
'''
Middleware for controller to contain all the modules
'''
import tornado.web
import tornado.escape
from tornado.gen import coroutine
from models.user import  user
					