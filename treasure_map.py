#I don't really think I need to upload this to GitHub

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

#take input and split it into a new list

test_letter = position[0].upper()
test_number = int(position[1])

standard_Number=["1","2","3"]
standard_List=["A", "B", "C"]

#compare the letter index 
test_letter_index = standard_List.index(test_letter)

#compare the number index
#note from the lesson example the columns in the greater matrix are accessed from outer to inner or n-1 terms. Since the column is going to be n <= 3 that's the max of the inputs that we can accept. 
test_number_index = test_number - 1


#lastly, use the map function to map the list without modifying them. Never mind she's calling the list of lists 'map'. 
map[test_number_index][test_letter_index] = "X"





# print("This is row:", row)

# input_list1 = str(position.split())
# input_list2 = int(input_list1)
# print(f"These are the results {input_list1}{input_list2}")

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

