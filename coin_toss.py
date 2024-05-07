import random

#detemrine the sequence variable for the toss
ran_sequence = random.randint(0,1)


#logic for sequence
if ran_sequence == 1:
	print("Heads")
else:
	print("Tails")