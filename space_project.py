#So this is an idea for a project that I had a few years ago but I
#couldn't get passed the logic in the last attempt that I made for the game. 

#So I'm going to re-design the game simulation to make it a space choice game.  Need to pull in mt assets. 

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




#game play turn 1
turn1 = input("Engage rocket boosters, yes or no?")

#turn 2
prompt1="Invading space army jumped out of hyperspeed."
turn2 = input("Hide or fight?")

#turn 3
prompt2="Hyperspeed point is coming up, you're off of the mark by 2 flight units"
final_turn = int(input("What do you do? 1.) Look for fuel, 2.) calculate route, 3.) or wait?"))

if turn1 == "yes" or "y":
	print(prompt1)
elif turn1 == "no" or "n":
	print("Hit by a comet. Game Over!")
else:
	"Mystery surprise: Game Over!"
# if turn1 == "yes" or "y":
# 	print(prompt1)
# 	if turn2 =="hide":
# 			print("Space invaders launched a missle and you're dead. Game Over!")
# 	elif turn2 == "fight":
# 			print(prompt2)
# 			if final_turn =="1":
# 				print("Ran out of fuel for the hyperspeed jump, float in space until your oxygen runs out. Game Over!")
# 			elif final_turn == "2":
# 				print("Inter-dimensional space snake exists a nearby wormhole and eats you whole. Game Over!")
# 			elif final_turn == "3":
# 				print("Lunar colony picked up your distress call andsentaid to your rescue. You win!")
# 			else:
# 				print("Mystery surprise: Game Over!")
# elif turn1 == "no" or "n":
# 	print("Hit by a comet. Game Over!")
# else:
# 	print("Mystery surprise: Game Over!")
