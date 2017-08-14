"""
Classmethods and staticmethods
1. Classmethods pass the class as the first argument automatically.
2. Staticmethods don't pass either instance or class as first argument.
"""

class Vehicle:

	increase_cost = 1.1 # In percentage

	def __init__(self, company, model, year, cost):
		self.company = company
		self.model = model
		self.year = year #Manufactured year
		self.cost = cost

	def raise_cost(self):
		self.cost = int(self.cost * self.increase_cost)

	@classmethod
	def set_increase_cost(cls, amount):
		cls.increase_cost = amount

	@staticmethod
	def num_tyres(tyres):
		


veh_1 = Vehicle('Mercedes-Benz', 'A 170 CDI', 2004, 200000)
veh_2 = Vehicle('Tesla', 'Model 3', 2017, 300000)

print(Vehicle.increase_cost)
Vehicle.set_increase_cost(1.5)
print(Vehicle.increase_cost)