mnorth = 1
meast = 3
north = 1
east = 3
note_walls = False
alone = False
armed = False
helmed = False
health = 1
no_notes = True
notes = []
inventory = []
first_floor = True
second_floor = False
third_floor = False
vested = False
BPV_visited = False
Crowbar_visited = False
barred = False
dreamworld_mumbai = False
Mumbai = False
dreamworld_paris = False
Paris = False
military_helmet = False
salted = False
smelling_salts = False
Mumbai_Dialogue = False
print("If you need help getting started, type 'help'")  
def movement():
  global north
  global east
  global action
  action = input("\n").capitalize()
  if action == "M":
    direction = input("\n\nWhich direction would you like to move? Type 'n' for north, 'e' for east, 's' for south, and 'w' for west: ").capitalize()
    if direction == "N":
      north += 1
      print("\n\nYou moved north 1 tile")
    elif direction == "S":
      north -= 1
      print("\n\nYou moved south 1 tile")
    elif direction == "E":
      east += 1
      print("\n\nYou moved east 1 tile")
    elif direction == "W":
      east -= 1
      print("\n\nYou moved west 1 tile")
  if action == "Help":
    print("'m' = move. Move north and talk to the secretary at the front desk.")

def mumbai_dream():
  global dreamworld_mumbai
  global alone
  global Mumbai_Dialogue
  global east
  global north
  global Mumbai
  global barred
  global armed
  global riddle_mumbai
  global notes
  global military_helmet
  global inventory
  global helmed
  print("\n\nAfter hooking yourself in, you find yourself in a Mumbai square. You spot the man from the room up ahead. You go to confront him.\nYou:\nWhat is the code to the room of your boss.\nHim: I can tell you the first half of the code if you answer my riddle: ")
  while True:  
    riddle_mumbai = input("\n\nThis is something rich people need, poor people have, brave people fear, and if you eat it you die: ").capitalize()
    if riddle_mumbai == "Nothing":
      print("\n\nThe man says coldly: 2-9.\n*Note Aqquired*\nYou shoot yourself and wake up, then leave the hotel room after grabbing a military helmet from the closet.")
      notes.append("2-9 is the first half.")
      Mumbai = True
      inventory.append("Helmet")
      helmed = True
      break
  third_floor_function()

def paris_dream(): 
  global dreamworld_paris
  global Paris
  global barred
  global armed
  global riddle_paris
  global notes
  global smelling_salts
  global inventory
  global salted
  print("\n\nAfter hooking yourself in, you find yourself in Paris. You spot the man from the room up ahead. You go to confront him.\nYou:What is the code to the room of your boss.\nHim: I can tell you the second half of the code if you answer my riddle.")
  while True:  
    riddle_paris = input("\n\nThe more of it there is, the less you see: ").capitalize()
    if riddle_paris == "Darkness":
      print("\n\nThe man says coldly: 1-3.\n*Note Aqquired*\nYou shoot yourself and wake up, then leave the hotel room after grabbing smelling salts from the closet.")
      notes.append("1-3 is the first half.")
      Paris = True
      inventory.append("salts")
      salted = True
      break
  third_floor_function()

def second_floor_function():
  global BPV_visited
  global Crowbar_visited
  global vested
  global barred
  while True:
    if second_floor == True:
      twofloorroom = input("\n\nWhich room would you like to enter? Enter '201', '202', '203', '204', or '205' or 'Exit': ").capitalize()
      if twofloorroom == "201" or twofloorroom == "202" or twofloorroom == "204":
        print("\n\nThis door is locked")
      if twofloorroom == "203":      
        if BPV_visited == True:
          print("\n\nYou've already been here.")
        if BPV_visited == False:
          print("\n\nYou enter an empty room with IDEA written on it. After a thorough search you find a bulletproof vest in the closet and add it to your inventory. You then leave the room.")
          vested = True
          BPV_visited = True
      if twofloorroom == "205":
        if Crowbar_visited == True:
          print("\n\nYou've already been here")
        if Crowbar_visited == False:      
          print("\n\nYou enter the room with the door already opened and see the room destroyed. In the center of the bed there is a crowbar and a note. You add the crowbar to your inventory.")
          print("\n\n*Note Aquired*")
          notes.append("I D E A")
          inventory.append("Crowbar")
          Crowbar_visited = True
          barred = True
      if twofloorroom == "Exit":
        ellie2()

def third_floor_function():
  global north
  global east
  global dreamworld_mumbai
  global dreamworld_paris
  while True:
    threefloorroom = input("\n\nAt the end of the hallway you see a Safe. Which room would you like to enter? Enter '301', '302', '303', '304', or '305', 'Safe' or 'Exit': ").capitalize()
    if threefloorroom == "301" or threefloorroom == "305":
      print("\n\nThis room is locked")  
    if threefloorroom == "302" and Mumbai == True:
      print("\n\nThere is no need to go in this room")
    if threefloorroom == "302" and Mumbai == False:
      print("\n\nYou see a man lying on the bed sleeping and a note that says: \"follow me if you want to know the code to room 303\". You see a dream machine on the bed beside the man with a second station ready.\nArthur: He knows you are here... We don't have much time. Get in there player!")
      ac1 = input("\n\n'Go' or 'Exit' (spell out word carefully): ").capitalize() 
      if ac1 == "Go":
        dreamworld_mumbai = True
        east = 3
        north = 1
        mumbai_dream()
        break
      if ac1 == "Exit":
        third_floor_function()
    if threefloorroom == "304"and Paris == False:
      print("\n\nYou see a man lying on the bed sleeping. Follow me if you want to know the code to room 303. You see a dream machine on the bed beside the man with a second station ready.\nArthur: He knows you are here... We don't have much time. Get in there player!")
      ac1 = input("\n\n'Go' or 'Exit' (spell out word carefully): ").capitalize()
      if ac1 == "Go":
        paris_dream()
      if ac1 == "Exit":
        third_floor_function()
    if threefloorroom == "304" and Paris == True:
        print("\n\nThere is no need to go in this room")
    if threefloorroom == "Exit":
        ellie3()
    if threefloorroom == "Safe":
      while True:
        safe = input("\n\nWhat is the safe combination (4 digits) or enter 'exit': ").capitalize()
        if safe == "Exit":  third_floor_function()
        if safe == "9451":
            print("\n\nThe safe opens to reveal a spinner that enlessly spins. You wake up in a cold sweat in an empty classroom with your monitor in front of you. You say, \"That was a crazy dream, time to get back to studying...\"")
            exit()
    if threefloorroom == "303":
      while True:
        pinlock = input("\n\nWhat is the 4 digit code or 'exit': ")
        if pinlock == "exit":  third_floor_function()
        if pinlock == "2913":
          print("\n\nArthur: Can you hear me? I can see from the window that the target is armed. Be careful.")
          if barred == True:
            print("\n\nYou break down the door with your crowbar")
            if vested == True:
              print("\n\nThe target attempts to unload a clip into your chest, but your vest protects you")
              if helmed == True:
                print("\n\nThe target shoots you at the helmet two times but their gun suddenly jams. So you use this opportunity and take the shot.")
                if salted == True:
                  print("\n\nThe smelling salts prevent you from identifying the target before you gun them down with your pistol./n/nArthur: Target is down! Good poop.\n\nMission accomplished!!!\n\nThanks for playing!!!\n\nTry to crack the code to the safe... your clue is \"I D E A\"")
                  exit()
                if salted == False:
                  print("\n\nAs you prepare to take your shot, you see that the target is Mal and hesitate, giving her a chance to unjam her weapon and hit your neck...")
                  print("\n\nM I S S O N - F A I L E D")
                  exit()
              if helmed == False:
                print("When you broke down the door your head had no protection and the target attacked you.")
                print("\n\nM I S S O N - F A I L E D")
                exit()
            if vested == False:
              print("As you break down the door, the target unloads a full clip into your chest.")     
              print("\n\nM I S S O N - F A I L E D")
              exit()
          if barred == False:
            print("\n\nYou try to open the door, it seems to be barricated. If only you had something to break it down with.")
            third_floor_function()
            exit()
def ellie1():
  global first_floor
  global second_floor
  global third_floor
  global north
  global east
  while True:
    if first_floor == True:
      elevator = input("\n\nWhich floor would you like to go to? Enter '1' for the first floor, '2' for the second or '3' for the third: ")
      if elevator == "1":
        print("\n\nNo time to fool around here, get going!")
      if elevator == "2":
        first_floor = False
        second_floor = True
        third_floor = False
        print("\n\n*Calming elevator music plays*\nPA: Second Floor.")
        second_floor_function()
        break
      if elevator == "3":
        first_floor = False
        second_floor = False
        third_floor = True
        north = 3 
        east = 2
        print("\n\n*Calming elevator music plays*\nPA: Third Floor.")
        third_floor_function()
        break

def ellie2():
  global first_floor
  global second_floor
  global third_floor
  global north
  global east
  while True:
    elevator = input("\n\nWhich floor would you like to go to? Enter '1' for the first floor, '2' for the second or '3' for the third: ")
    if elevator == "2":
      second_floor_function()
    if elevator == "1":
      print("\n\nYou try to press the button again and again, but it seems to be jammed. ")
    if elevator == "3":
      first_floor = False
      second_floor = False
      third_floor = True
      north = 3 
      east = 2
      print("\n\n*Calming elevator music plays*\nPA: Third Floor.")
      third_floor_function()
      break
      
def ellie3():
  global first_floor
  global second_floor
  global third_floor
  global north
  global east
  while True:
    elevator = input("\n\nWhich floor would you like to go to? Enter '1' for the first floor, '2' for the second or '3' for the third: ")
    if elevator == "3":
      third_floor_function()
    if elevator == "1":
      print("\n\nYou try to press the button again and again, but it seems to be jammed. ")
    if elevator == "2":
      print("\n\n*Calming elevator music plays*\nPA: Third Floor.")
      first_floor = False
      second_floor = True
      third_floor = False
      north = 3
      east = 2
      second_floor_function()
      break

print("\nYou have been sent here to assassinate a target. All you need to know is that they are wearing black and in no way will this mission be easy because they are very skilled and diligent. We appreciate your great service to humanity, and we wish you luck.\n")
print("Arthur: Have you established contact?\nYou: Yes, I am in the middle of the lobby.\nArthur: The target is in the same building, I am monitoring you from a nearby window. See if you can find a clue as to which room he is in. Over and out.\n")

while True:
  movement()

  if (east == 0 or east == 6 or north == 6 or north == 0) and first_floor == True:
    print ("\n\nYou crashed into a wall! Check your notes (to check notes type 'n').")
    if note_walls == False:
      notes.append("You can't walk into walls good sir")
      note_walls = True
      no_notes = False
    if east == 0:
      east = 1
    if east == 6:
      east = 5
    if north == 6:
      north = 5
    if north == 0:
      north = 1
    note_walls == True
    
  if north == 3 and east == 3 and first_floor == True:
    print("\n\n*You see the main desk and walk up to it*\nYou: I'm looking for a man in a Black Suit.\nSecretary: Well if he is in a black suit, he will be on the 3rd floor\n*Note Aquired*\nJust keep heading west until you reach the elevator.")
    no_notes = False
    notes.append("The target is on the third floor.")
  
  if north == 3 and east == 1:
    elevator_prompt = input("\n\nYou see an elevator, would you like to go in? Type 'Y' for yes  and 'N' for no: ").capitalize()
    if elevator_prompt == "Y":
      ellie1()
    else:
      east = 2
      north = 3