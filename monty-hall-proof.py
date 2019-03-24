import sys
import math
import random
import argparse

parser = argparse.ArgumentParser(description='A program to prove the Monty Hall problem.')
parser.add_argument('-p','--play-game',action='store_true',dest='playGame',help='switch to enable live game play')
parser.add_argument('-t','--total-games',action='store',dest='totalGames',default=1000000,metavar='TG',type=int,help='the total number of games the simulator will run (default: 1000000)')
parser.add_argument('-v','--verbose',action='store_true',help='switch to enable verbose print statements')

args = parser.parse_args()

if(args.playGame and not args.verbose):
	args.verbose = True

class Door:

	def __init__(self,number,status,hasCar,isChosen):
		self.number = number
		self.status = status
		self.hasCar = hasCar
		self.isChosen = isChosen

	def open(self):
		if(self.status == 'open'):
			if(args.verbose):
				print('ERROR: Door ' + str(self.number) + ' is already ' + self.status)
				sys.exit()
		else:
			self.status = 'open'

			if(self.hasCar):
				if(args.verbose):
					print('Winner!  Door ' + str(self.number) + ' has a car behind it')
			else:
				if(args.verbose):
					print('Door ' + str(self.number) + ' is open and has a goat')

	def choose(self):
		if(self.isChosen):
			print('ERROR: Door ' + str(self.number) + ' is already chosen')
			sys.exit()
		else:
			self.isChosen = True

			if(args.verbose):
					print('Door ' + str(self.number) + ' has been chosen')

	def unchoose(self):
		if(not self.isChosen):
			print('ERROR: Door ' + str(self.number) + ' is not chosen already')
			sys.exit()
		else:
			self.isChosen = False

	def printDoor(self):
		if(args.verbose):
			print('Door ' + str(self.number) + ' is ' + self.status)

# Helper methods

def printInstructions(playGame):
	print('Imagine you\'re on a game show, and you\'re given the choice of three doors.')
	print('Behind one door is a car; behind the others, goats.')
	print('You can choose any door that you wish, then the host will reveal one of the losing doors.')
	print('Next, you will be given the chance to switch your original choice with the remaining door, but is that in your best interest?')

	if(playGame):
		print('Can you win the car?')
		print('Godd luck!')
		print('------------------------------------------------------------------------------------------------------------------------')
		print('Type \'exit\' at any time to quit the game.')
	
	print('------------------------------------------------------------------------------------------------------------------------')

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

def chooseDoor(doors,userInput):
	if(userInput == None):
		userInput = random.randint(1,3)

	for door in doors:
		if(door.number == userInput):
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
			if(args.verbose):
				print('Sorry, Door ' + str(door.number) + ' has a goat')
			return False

def printResults(totalGames,numStayed,numWinsStayed,numSwitched,numWinsSwitched):
	if(totalGames == 0):
		return

	if(args.playGame):
		print('------------------------------------------------------------------------------------------------------------------------')

	print('Monty Hall Problem Results')
	print('------------------------------------------------------------------------------------------------------------------------')
	print('Total games played: ' + str(totalGames))
	print('------------------------------------------------------------------------------------------------------------------------')

	if(numStayed == 0):
		print('No games where original door was kept')
	else:
		print('Expected winning percentage when keeping original door: 33%')
		print('Actual winning percentage when keeping original door: ' + str(math.trunc((numWinsStayed / numStayed) * 100)) + '%')

	print('------------------------------------------------------------------------------------------------------------------------')
	
	if(numSwitched == 0):
		print('No games where original door was switched for remaining dooru')
	else:
		print('Expected winning percentage when switching doors: 66%')
		print('Actual winning percentage when switching doors: ' + str(math.trunc((numWinsSwitched / numSwitched) * 100)) + '%')
	
	print('------------------------------------------------------------------------------------------------------------------------')

# Main program logic

print('------------------------------------------------------------------------------------------------------------------------')
print('Let\'s Make a Deal!')
print('------------------------------------------------------------------------------------------------------------------------')
printInstructions(args.playGame)

if(args.playGame):
	totalGames = 0
	numSwitched = 0
	numWinsSwitched = 0
	numStayed = 0
	numWinsStayed = 0

	while True:
		didSwitch = False
		doors = setupDoors()

		while True:
			userInput = input('Please choose a door: ')
			if(userInput.lower() == 'exit'):
				printResults(totalGames,numStayed,numWinsStayed,numSwitched,numWinsSwitched)
				print('Thanks for playing!')
				sys.exit()
			elif(not userInput.isdigit() or not userInput in ['1','2','3']):
				print('ERROR: Value entered must be a number between 1 and 3')
			else:
				break

		chooseDoor(doors,int(userInput))
		remainingUnchosenDoor = revealLosingDoor(doors)

		while True:
			switch = input('Would you like to switch Door ' + userInput + ' with Door ' + str
				(remainingUnchosenDoor.number) + '? Type \'y\' for yes, \'n\' for no: ')
			if(not switch.lower() in ['y','n','exit']):
				print('ERROR: Value entered must be \'y\', \'n\', or \'exit\'')
			elif(switch.lower() == 'y'):
				didSwitch = True
				switchDoor(doors,remainingUnchosenDoor)
				numSwitched += 1
				break
			elif(switch.lower() == 'exit'):
				printResults(totalGames,numStayed,numWinsStayed,numSwitched,numWinsSwitched)
				print('Thanks for playing!')
				print('------------------------------------------------------------------------------------------------------------------------')
				sys.exit()
			else:
				numStayed += 1
				break

		totalGames += 1

		if(isWinner(doors)):
			if(didSwitch):
				numWinsSwitched += 1
			else:
				numWinsStayed += 1

		while True:
			playAgain = input('Play again? Type \'y\' for yes, \'n\' for no: ')
			if(not playAgain.lower() in ['y','n','exit']):
				print('ERROR: Value entered must be \'y\', \'n\', or \'exit\'')
			elif(playAgain.lower() == 'n' or playAgain.lower() == 'exit'):
				printResults(totalGames,numStayed,numWinsStayed,numSwitched,numWinsSwitched)
				print('Thanks for playing!')
				print('------------------------------------------------------------------------------------------------------------------------')
				sys.exit()
			else:
				break
else:
	numStayed = 0
	numWinsStayed = 0

	print('Simulating keeping original door ' + str(args.totalGames) + ' time(s)')
	print('------------------------------------------------------------------------------------------------------------------------')

	for x in range(args.totalGames):
		if(args.verbose):
			print('----------')
			print('Game ' + str(x + 1))
			print('----------')

		doors = setupDoors()
		chooseDoor(doors,None)
		revealLosingDoor(doors)
		if(isWinner(doors)):
			numWinsStayed += 1
		numStayed += 1

	numSwitched = 0
	numWinsSwitched = 0

	print('Simulating switching door ' + str(args.totalGames) + ' time(s)')
	print('------------------------------------------------------------------------------------------------------------------------')

	for x in range(args.totalGames):
		if(args.verbose):
			print('----------')
			print('Game ' + str(x + 1))
			print('----------')

		doors = setupDoors()
		chooseDoor(doors,None)
		remainingUnchosenDoor = revealLosingDoor(doors)
		switchDoor(doors,remainingUnchosenDoor)
		if(isWinner(doors)):
			numWinsSwitched += 1
		numSwitched += 1

	printResults(args.totalGames,numStayed,numWinsStayed,numSwitched,numWinsSwitched)