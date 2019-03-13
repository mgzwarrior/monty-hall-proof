import sys
import math
import random

if(len(sys.argv) < 3):
	print('ERROR: Invalid arguments - see README for running instructions')
	sys.exit()
totalGames = int(sys.argv[1])
suppressPrintStatements = bool(sys.argv[2])

class Door:

	def __init__(self,number,status,hasCar,isChosen):
		self.number = number
		self.status = status
		self.hasCar = hasCar
		self.isChosen = isChosen

	def open(self):
		if(self.status == 'open'):
			if(not suppressPrintStatements):
				print('ERROR: Door ' + str(self.number) + ' is already ' + self.status)
				sys.exit()
		else:
			self.status = 'open'

			if(self.hasCar):
				if(not suppressPrintStatements):
					print('Winner!  Door ' + str(self.number) + ' has a car behind it')
			else:
				if(not suppressPrintStatements):
					print('Door ' + str(self.number) + ' is open and empty')

	def choose(self):
		if(self.isChosen):
			print('ERROR: Door ' + str(self.number) + ' is already chosen')
			sys.exit()
		else:
			self.isChosen = True

			if(not suppressPrintStatements):
					print('Door ' + str(self.number) + ' has been chosen')

	def unchoose(self):
		if(not self.isChosen):
			print('ERROR: Door ' + str(self.number) + ' is not chosen already')
			sys.exit()
		else:
			self.isChosen = True

	def printDoor(self):
		if(not suppressPrintStatements):
			print('Door ' + str(self.number) + ' is ' + self.status)

def setupDoors():
	door1 = Door(1,'closed',False,False)
	door2 = Door(2,'closed',False,False)
	door3 = Door(3,'closed',False,False)
	doors = [door1,door2,door3]

	ran = random.randint(1,3)

	for door in doors:
		if(door.number == ran):
			door.hasCar = True

		door.printDoor()

	return doors

def chooseDoor(doors):
	ran = random.randint(1,3)

	for door in doors:
		if(door.number == ran):
			door.choose()
			break

def revealLosingDoor(doors):
	unchosenDoors = []
	revealedDoor = None

	for door in doors:
		if(door.isChosen):
			continue
		unchosenDoors.append(door)

	for door in unchosenDoors:
		if(door.hasCar):
			continue
		
		revealedDoor = door
		revealedDoor.open()
		unchosenDoors.remove(door)

	return unchosenDoors.pop()

def switchDoor(doors,remainingUnchosenDoor):
	for door in doors:
		if(door.isChosen):
			door.unchoose()
			break

	remainingUnchosenDoor.choose()

def isWinner(doors):
	for door in doors:
		if(door.isChosen and door.hasCar):
			door.open()
			return True
		if(door.isChosen and not door.hasCar):
			if(not suppressPrintStatements):
				print('Sorry, Door ' + str(door.number) + ' is empty')
			return False

numWins = 0

for x in range(totalGames):
	suppressPrintStatements = True
	doors = setupDoors()
	chooseDoor(doors)
	remainingUnchosenDoor = revealLosingDoor(doors)
	switchDoor(doors,remainingUnchosenDoor)
	if(isWinner(doors)):
		numWins += 1

print('Winning percentage when switching doors: ' + str(math.trunc((numWins / totalGames) * 100)) + '%')

numWins = 0

for x in range(totalGames):
	suppressPrintStatements = True
	doors = setupDoors()
	chooseDoor(doors)
	revealLosingDoor(doors)
	if(isWinner(doors)):
		numWins += 1

print('Winning percentage when keeping original door: ' + str(math.trunc((numWins / totalGames) * 100)) + '%')