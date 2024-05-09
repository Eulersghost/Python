line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

#take input and split it into a new list

x= postion.split()

y = map(int, x.split())
# print("This is row:", row)
print("This is column:", column)
# input_list1 = str(position.split())
# input_list2 = int(input_list1)
# print(f"These are the results {input_list1}{input_list2}")

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

