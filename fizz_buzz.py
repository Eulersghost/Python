#This is the start of the Fizz Buzz exercise I've already done this in JS so I'll just reference that. 


count = 100

for number in range(1, count+1):
	if number % 3 == 0 and number % 5 == 0:
		print("FizzBuzz")
	elif number % 3 == 0:
		print("Fizz")
	elif number % 5 == 0:
		print ("Buzz")
	else:
		print(number)