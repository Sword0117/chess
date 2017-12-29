from configurations import *
import model

class Controller():
	def __init__(self):
		self.init_model()

	def init_model(self): 
		# instantiated a new Model class within controller class
		# A way of controller to interact with model
		self.model = model.Model()