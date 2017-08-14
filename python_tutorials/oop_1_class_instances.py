"""
1. Class is used to group functions and methods.
2. Can be rebuild easily based on requirements.
3. Used to write reusable code.
"""

class Employee:
	"""
	Employee class 
	"""

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def display_name(self):
		return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Ravikiran', 'Talluri', 50000)
emp_2 = Employee('Raviteja', 'Talluri', 100000)

print(emp_2.display_name())
