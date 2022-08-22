
class elevator(): #defining elevator characteristics
  def __init__(self, currentFloor = 1, serviceMode = False, maxHeight = 20, minHeight = 1):
    self.currentFloor = currentFloor
    self.inServiceMode = serviceMode
    self.maxHeight = maxHeight
    self.minHeight = minHeight
  
  def goToFloor(self, move): #method that moves elevator
    if move >= self.minHeight and move <= self.maxHeight: #checks movement range
      if self.inServiceMode == False: #checks mode
        self.currentFloor = move
        print("The elevator moved to " + str(self.currentFloor) + ".")
      else:
        print("Elevator in service mode.")
    else:
      print("Floor out of range.")

  def __str__(self): #returns elevator information
    if(self.inServiceMode):
      return "SERVICE MODE: The elevator is in service on floor " + str(self.currentFloor) + "."
    else:
      return "The elevator is on floor " + str(self.currentFloor) + "."

class smartElevator(elevator): #Smart elevator characteristics
  def __init__(self, currentFloor = 1, serviceMode = False, maxHeight = 20, minHeight = 1):
    super().__init__(currentFloor, serviceMode)
    
  def goToFloor(self, move): #method moves and shows elevator moving
    if move >= self.minHeight and move <= self.maxHeight: #checks movement range  
      if self.inServiceMode == False: #checks mode
        if self.currentFloor != move:
          while self.currentFloor != move:
            if self.currentFloor < move:
              self.currentFloor += 1
              print(self.currentFloor)
            elif self.currentFloor > move:
              self.currentFloor -= 1
              print(self.currentFloor)
          print("The elevator moved to floor " + str(self.currentFloor) + ".")
    
        elif self.currentFloor == move:
          self.currentFloor = move

      else:
        print("SERVICE MODE: Elevator in service mode on floor" + self.currentFloor + ".")
    else: 
      print("Floor out of range.")

#running elevator
print("Elevator:")
print()
elevator = elevator()
print(elevator)
elevator.goToFloor(7)
print(elevator)
elevator.goToFloor(7)
elevator.goToFloor(-4)
elevator.inServiceMode = True
print(elevator)
elevator.goToFloor(6)
elevator.goToFloor(21)
elevator.inServiceMode = False
elevator.goToFloor(20)
print(elevator)
print()

#running smartElevator
print("Smart Elevator:")
print()
smartElevator = smartElevator()
print(smartElevator)
smartElevator.goToFloor(7)
print(smartElevator)
smartElevator.goToFloor(3)
smartElevator.goToFloor(3)


