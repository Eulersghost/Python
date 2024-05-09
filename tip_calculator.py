#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#use the round(a,b) method where a = the number being rounded, and b equals the number of digit spaces.

#Write your code below this line 👇


#1. prompt user for the bill and set it so that it has only two decimal spots for the input

print("What was the total amount for the bill?")
input_bill = round(float(input()),2)
print("How much tip do you want to add, 10, 12,15, or 20%?")
input_tip = round(float(input()),2)
print("How many people to split the check?")
input_people = int(input())

#2. need to calculate the tip portion
total_tip = (input_tip * 0.01) * input_bill

#3. add tip to bill
tip_and_bill = total_tip + input_bill

#4. now split it with the amount of people
total = tip_and_bill/input_people

#5. output the final result
grand_total = round(total,2)

print(f"Each person needs to pay ${grand_total} dollars")
