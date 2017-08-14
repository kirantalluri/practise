"""
1. Class variables are the variables that are shared among all instances of a class. 
2. Class variables should be the same for all instances unlike instance variables.
3. Class variable can be accessed using instances.

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


veh_1 = Vehicle('Mercedes-Benz', 'A 170 CDI', 2004, 200000)
veh_2 = Vehicle('Tesla', 'Model 3', 2017, 300000)

# print('Before assigning new value')
# print(Vehicle.increase_cost)
# print(Vehicle.__dict__)

# print('After assigning new value')
# Vehicle.increase_cost = 1.5
# print(Vehicle.increase_cost)
# print(Vehicle.__dict__)

# print('Accessing class variable using instance')
# print(veh_1.increase_cost)
# print(veh_1.__dict__)

# veh_2.increase_cost = 1.2
# print(veh_2.increase_cost)
# print('increase_cost is now present in the company space of veh_2 instance')
# print(veh_2.__dict__)

# print(Vehicle.increase_cost)
