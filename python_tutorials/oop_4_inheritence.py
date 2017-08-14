"""
Inheritence
1. We can inherit attributes and methods from parent class
2. Used to inherit all methods and attributes to subclass without effecting parent class
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


class Car(Vehicle, object):
	
	increase_cost = 1.2

	def __init__(self, company, model, year, cost, car_type):
		super(Car, self).__init__(company, model, year, cost)
		self.car_type = car_type


class Truck(Vehicle, object):

	increase_cost = 1.5

	def __init__(self, company, model, year, cost, truck_type):
		super(Truck, self).__init__(company, model, year, cost)
		self.truck_type = truck_type


car_1 = Car('Mercedes-Benz', 'A 170 CDI', 2004, 200000, 'Sudan')
trk_1 = Truck('Mercedes-Benz', 'A 170 CDI', 2004, 200000, 'Heavy Vehicle')

# print(car_1.company)
# print(car_1.car_type)

# print(isinstance(trk_1, Car))
# print(issubclass(Truck, Vehicle))

# car_1 = Car('Mercedes-Benz', 'A 170 CDI', 2004, 200000)
# car_1.raise_cost()
# print(car_1.cost)

# print(help(Car)) # Use this for visualizing the class

# print(car_1.company)
