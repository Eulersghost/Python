#looks like I need to create a function that takes an input from someone and stores it in a list.
#import the random module
import random


test_input = input("Whose turn is it to pay the bill, enter your names? ")
#1. first step is to create an empty list

names = test_input.split(", ")

#initialize random module
list_choice = random.choice(names)

# print(list_choice)

#2. define logic for list

if len(names) < 30:
	print(f"{list_choice} is going to buy the meal today!")
else:
	print("Just pay the bill!")


#in the lesson answer she coded the random choice as 
#num_items = len(names)
#random_choice = random.randint(0,num_items-1)
#print(name[random_choice])˛˛