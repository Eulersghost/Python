#So this is an idea for a project that I had a few years ago but I
#couldn't get passed the logic in the last attempt that I made for the game. 

#So I'm going to re-design the game simulation to make it a space choice game.  Need to pull in mt assets. 

import sys


print(r'''   
                  .-.
   .-""`""-.    |(@ @)
_/`oOoOoOoOo`\_ \ \-/
'.-=-=-=-=-=-=-.' \/ \
  `-=.=-.-=.=-'    \ /\
     ^  ^  ^       _H_ \



                }--O--{
                  [^]
                 /ooo\
 ______________:/o   o\:______________
|=|=|=|=|=|=|:A|":|||:"|A:|=|=|=|=|=|=|
^""""""""""""""!::{o}::!""""""""""""""^
                \     /
                 \.../
      ____       "---"       ____
     |\/\/|=======|*|=======|\/\/|
     :----"       /-\       "----:
                 /ooo\
                #|ooo|#
                 \___/

    ''')


#Print the game intro

print("Welcome to space oddessy:  Your mission just launched from Orbital 1 station your mission is to get to lunar colony on the moon of Titan.  Alive...and in one piece.")




#turn 1
turn1 = input("Engage rocket boosters, yes or no? \n")
turn1_lower = turn1.lower()

if turn1_lower== "yes" or turn1_lower == "y" or turn1_lower == "YES":
  print("Invading space army jumped out of hyperspeed. \n")
elif turn1_lower == "no" or turn1_lower == 'n' or turn1_lower == "NO":
  print("Hit by a comet. Game Over! \n")
  sys.exit()
elif turn1 and turn1 != ("yes" or "no"):
  print("Mystery surprise: Game Over! \n")
  sys.exit()
else:
  print("Game Over")
  sys.exit()

#turn 2
turn2 = input("Hide or fight? \n")
turn2_lower = turn2.lower()

if turn2_lower == "Hide" or turn2_lower == "hide" or turn2_lower == "HIDE":
  print("Space invaders launched a missle and you're dead. Game Over! \n")
  sys.exit()
elif turn2_lower == "Fight" or turn2_lower == "fight" or turn2_lower =="FIGHT":
  print("Hyperspeed point is coming up, you're off of the mark by 2 flight units \n")
elif turn2 != ("fight" or "hide"):
  print("Mystery surprise: Game Over! \n")
  sys.exit()
else:
  print("Game Over")
  sys.exit()


# turn 3
final_turn = int(input("What do you do? Enter the following numbers: 1.) Look for fuel, 2.) calculate route, 3.) or wait? \n"))

if final_turn == 1:
  print("Ran out of fuel for the hyperspeed jump, float in space until your oxygen runs out. Game Over!")
  sys.exit()
elif final_turn == 2:
  print("Inter-dimensional space snake exists a nearby wormhole and eats you whole. Game Over!\n")
  sys.exit()
elif final_turn == 3:
  print("Lunar colony picked up your distress call and sent aid to your rescue. You win! \n")
else:
  print("Game Over")
  sys.exit()
