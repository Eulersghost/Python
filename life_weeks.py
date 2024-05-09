age = input()
# ? Don't change the code above ?
# Write your code below this line ?

#So the total of the weeks will be 4680 given that there's 52 weeks in a year. Which means
#50*90


#1. Set grand total weeks 
g_total = 4680

#2. Need to have a conversion of input to int

age_convert = int(age)


#3. for any age input multiply by 52 which will get total 

w_convert = age_convert * 52 

#4. subtract inputted weeks conversion from g_total

total = g_total - w_convert 

print (f"You have {total} weeks left")

