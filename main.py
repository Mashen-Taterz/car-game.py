### Car Game ###

#attempt with no help 
'''run_game = True
user_input = input()

start_car = "The car has started... Let's go!"
stop_car = "The car has stopped."
options = "Start: Start the Car\nStop: Stop the car\nQuit: End the game"

while run_game:
  if user_input == "start".upper:
    print(start_car)
  elif user_input == "stop".upper:
    print(stop_car)
  elif user_input == "help".upper:
    print(options)
  elif user_input == "quit".upper:
    print("Game Over")
  else:
    print("Type 'help' for more options.")
    break

run_game = False'''

#Solution
command = ""
started = False
while True:
  command = input("> ").lower()
  if command == "start":
    if started:
      print("Car already started!")
    else:
      started = True
      print("Car has started.")
  elif command == "stop":
    if started == False:
      print("The car is already stopped!")
    else:
      started = False
      print("The car has stopped!")
  elif command == "help":
    print ("""
start - to start the car.
stop - to stop the car.
quit - to end the game.
    """)
  elif command == "quit":
    break
  else:
    print("I do not understand. Try help for more options.")
  
  



