# S - $15, M - $20, L - $25

# Extras: Pepperoni for small is extra $2

# Pepperoni for M/L is $3

# Extra cheese is $1

print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? S, M, or L
add_pepperoni = input()  # Do you want pepperoni? Y or N
extra_cheese = input()  # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇


total_cost = 0


if size == "S":
  total_cost += 15
elif size == "M":
  total_cost += 20
else:
  total_cost += 25


if add_pepperoni == "Y":
  if size == "S":
    total_cost += 2
  else:
    total_cost += 3

if extra_cheese == "Y":
  total_cost += 1

print(f"Your final bill is: ${total_cost}.")
