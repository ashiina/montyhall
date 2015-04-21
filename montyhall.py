
import sys
import random

class MontyHall:
	CORRECT = 1
	doors = [0,0,0]
	correctDoor = 0
	chosenDoor = 0
	emptyDoor = 0
	shouldChangeDoor = 0

	def __init__(self, chosenDoor, shouldChangeDoor):
		self.chosenDoor = int(chosenDoor)
		self.shouldChangeDoor = str(shouldChangeDoor)
	def populateDoors(self):
		self.correctDoor = random.randint(0,2);
		self.doors[self.correctDoor] = MontyHall.CORRECT
	def getEmptyDoor(self):
		for i in range(0,3):
			if self.doors[i] != MontyHall.CORRECT and i != self.chosenDoor:
				self.emptyDoor = i
				return self.emptyDoor
	def changeChosenDoor(self):
		for i in range(0,3):
			if i != self.emptyDoor and i != self.chosenDoor:
				self.chosenDoor = i
#				print "changed door:%s" % self.chosenDoor
				return self.chosenDoor
	def openDoor(self, targetDoor):
		if self.doors[targetDoor] == MontyHall.CORRECT:
			print "Correct"
		else:
			print "Wrong"

	def run(self):
		self.populateDoors()
#		print "Doors: %s" % self.doors
#		print "Chose door:%s" % self.chosenDoor
		openDoor = self.getEmptyDoor()
#		print "open door:%s" % openDoor
#		response = raw_input("change door?")
#		print "response:%s" % response
#		if response == "y":
		if self.shouldChangeDoor == "y":
			self.changeChosenDoor()
		self.openDoor(self.chosenDoor)

# ------
# run script with args: 
# python montyhall.py {door_index:0,1,2} {change_door:y|n}
mh = MontyHall(sys.argv[1], sys.argv[2])
mh.run()


