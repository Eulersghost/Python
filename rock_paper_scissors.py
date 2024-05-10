#below is the rock paper scissors game, I've done this before but I'm going to re-do it as a second iteration

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#import necessary packages/modules
import random

#convert variables to an easily accessible list
randomList = [rock,paper,scissors]

#setup random choice module
rChoice = random.choice(randomList)

#capture user input
player_choice = input("Enter a choice type rock, paper, scissors: ")

if rChoice == rock:
	print("Computer chose rock \n", rock)
elif rChoice == paper:
	print("Computer chose paper \n", paper)
elif rChoice == scissors:
	print("Computer chose scissors \n", scissors)
else:
	print("Error!")


#define player logic for different cases

if player_choice == "rock" or "Rock" or "ROCK" and rChoice == scissors:
	print ("You win!")
elif player_choice == "scissors" or "Scissors" or "SCISSORS" and rChoice == paper:
	print("You win!")
elif player_choice == "paper" or "Paper" or "PAPER" and rChoice == rock:
	print("You win!")
else:
	print("You loose!")


