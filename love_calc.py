
# need to create a method that captures my input and counts the characters in a string and compares it to 'love ' and 'true'

first = input("enter your name \n")
second = input("enter there name \n")
# define count function

my_input = first.lower()
there_input = second.lower()

arg1 = my_input.count("t")
arg2 = my_input.count("r")
arg3 = my_input.count("u")
arg4 = my_input.count("e")
arg9 = there_input.count("t")
arg10 = there_input.count("r")
arg11 = there_input.count("u")
arg12 = there_input.count("e")
arg5 = my_input.count("l")
arg6 = my_input.count("o")
arg7 = my_input.count("v")
arg8 = my_input.count("e") 
arg13 = there_input.count("l")
arg14 = there_input.count("o")
arg15 = there_input.count("v")
arg16 = there_input.count("e")

t1 = arg1+arg2+arg3+arg4
t2 = arg9+arg10+arg11+arg12
true_final = t1+t2

t3 = arg5+arg6+arg7+arg8
t4 = arg13+arg14+arg15+arg16
love_final = t3+t4

total = int(str(true_final) + str(love_final))
# print (f"true = {true_final}")
# print(f"love = {love_final}")


# total = f"{true_final}{love_final}"

# print(total)


#define the logic for the 'love calculator'

if total < 10 or total > 90:
	print(f"Your score is {total}, you go together like coke and mentos.")
elif total >=40 and total <=50:
	print(f"Your score is {total}, you are alright together.")
else:
	print(f"Your score is {total}.")