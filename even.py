#capture the input

user_input = int(input())


#initialize an accumulator
counter = 0 

var = range(0, user_input+1, 2)

#start the counter 
for x in var:
	if x%2 == 0:
		counter += x

print(counter)


	
