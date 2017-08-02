import logging


logging.basicConfig(filename='course.log', 
		    level=logging.DEBUG)


class Course:

    """
    Class Course which contains all
    necessary information regarding a 
    course
    """

    def __init__(self, name, hours_needed, fee):
	self.name = name
	self.hours_needed = hours_needed
	self.fee = fee
 
    @property
    def name(self):
	return self.name

    @name.setter
    def name(self, name):
	self.name = name

    @property
    def desc(self):
	return '{}: This subject is needed to attain great knowledge.'.format(self.name)

    #def __repr__(self):
#	return '{} - {} - {}'.format(self.name, self.hours_needed, self.fee)


class Staff(Course):

    """
    Class Staff is used for assging staff to each courses.
    """

    def __init__(self, name, hours_needed, fee, staff_name, salary):
	Course.__init__(self, name, hours_needed, fee)
	self.staff_name = staff_name
	self.salary = salary

    def raise_amount(self, raise_percent=1):
	return int(self.salary * raise_percent)

    #def __repr__(self):
#	return '{} {} {}'.format(self.name , self.staff_name, self.hours_needed)


#print(help(Staff))

crs_1 = Staff('python', 100, 1000, 'Ravikiran', '2000')
crs_2 = Staff('java', 1000, 100000, 'Naveen', '3000')
#crs_2.name = 'Erlang'
print(crs_1.desc)
print(crs_2.desc)

#print(crs_1)
#print(crs_2)

logging.info('Python Course instance: {}'.format(crs_1.name))
logging.info('Java Course instance: {}'.format(crs_2.name))

