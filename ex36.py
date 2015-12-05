from sys import exit

def first_room():
  # first_room - 3 choices leading to exit or back to the main room.
  print "You step through the door into a well lit room."
  print "There is a large ticking bomb on a table in front of you."
  print "There is a multitool next to the bomb."
  print "You can cut the red wire, the blue wire, or smash the bomb."
  print "Which do you do?"
  choice = raw_input ("> ")

  if "red" in choice:
    print "You cut the red wire."
    print "The bomb explodes in your face and you die."
    exit(0)
  elif "blue" in choice:
    print "You cut the blue wire."
    print "The bomb stops ticking.  You step back into the main room."
    main_room()
  elif "smash" in choice:
    print "You smash the bomb on the floor."
    print "The bomb explodes in your face and you die."
    exit(0)
  else:
    dead("You made the wrong choice.")

def second_room():
  #second room leads to death from first room's bomb
  print "You choose the second door."
  print "You approach the door and find it locked."
  print "While pulling on the handle to get it open the bomb in room 1 goes off."
  print "You lose an arm and slowly bleed to death on the floor."
  exit(0)

def third_room():
  #find a tiger, leads to exit or back to main room
  print "You walk in to a dim room and see a tiger sleeping on the floor."
  print "The tiger is snoring and you decide what to do."
  print "You can kick the tiger, pet the tiger, or leave quietly."
  print "Which do you do?"

  choice = raw_input ("> ")

  if "kick" in choice:
    print "You walk up and kick the tiger in it's stupid head."
    print "The tiger wakes up and eats you."
    exit(0)
  elif "pet" in choice:
    print "You walk up carefully and pet the tiger."
    print "The tiger wakes up and eats you."
    exit(0)
  elif "leave" in choice:
    print "You slowly back through the door and pull it closed."
    main_room()
  else:
    dead ("You made the wrong choice.")

def fourth_room():
  #fall through some spikes and die
  print "You push through the fourth door feeling like you "
  print "made the right choice.  Instead, you fall through a trap door"
  print "onto some spikes and you die slowly bleeding out."
  print "good bye!"
  exit(0)

def dead(why):
  # ask to end or continue, function leads back to main_room or to an exit
  print why
  print "end or continue?"
  choice = raw_input("> ")
  if choice == "end":
    print "Thanks for playing."
    exit(0)
  elif choice == "continue":
    print "Let's go again!"
    main_room()
  else:
    print("total douche...")
    exit(0)

def main_room():
  # main_room function will call the other room functions based on user choice

  print "You walk into a small room with 4 doors labeled 1-4."
  print "You cannot go back the way you came so you must choose a door."
  print "Which do you choose to enter: first, second, third, or fourth?"
  
  #get user's main room choice
  choice = raw_input("> ")

  #act on user's main room choice
  if choice == "first":
    first_room()
  elif choice == "second":
    second_room()
  elif choice == "third":
    third_room()
  elif choice == "fourth":
    fourth_room()
  else:
    dead("Don't be a douche, enter a correct value")

main_room()