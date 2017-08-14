"""
Getters and Setters
1. We can define them using @property decorator in python
2. Comes in handy when we need to define a method and access it as a variable
"""

class Vehicle:

	annual_increase = 1.1 # In percentage

	def __init__(self, company, model, year):
		self.company = company
		self.model = model
		self.year = year #Manufactured year
		
	@property
	def cost(self, cost):
		self.cost = cost


veh_1 = Vehicle('Mercedes-Benz', 'A 170 CDI', 2004)
veh_1.cost = 2000
print(veh_1.cost)

