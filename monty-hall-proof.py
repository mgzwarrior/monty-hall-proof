import random

class Door:

	def __init__(self,number,status,hasCar):
		self.number = number
		self.status = status
		self.hasCar = hasCar

	def open(self):
		if(self.status == 'open'):
			print('Door ' + str(self.number) + ' is already ' + self.status)
		else:
			self.status = 'open'

	def close(self):
		if(self.status == 'closed'):
			print('Door ' + str(self.number) + ' is already ' + self.status)
		else:
			self.status = 'closed'

	def printDoor(self):
		print('Door ' + str(self.number) + ' is ' + self.status)

door1 = Door(1,'closed',False)
door2 = Door(2,'closed',False)
door3 = Door(3,'closed',False)

print(random.randint(1,3))