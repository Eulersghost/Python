# Input a Python list of student heights
student_heights = input().split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇


#1. grab the length of the list and convert to an int

# len_int_convert = int(len(student_heights))

len_counter = 0
for x in student_heights:
  len_counter += 1

#2. convert the input list to a integer

#studentSum = int(sum(student_heights))

studentSum = 0
for y in student_heights:
  studentSum = studentSum + y

#3. average the results together

totalSum = round(studentSum / len_counter)


print(f"total height = {studentSum}")
print(f"number of students = {len_counter}")
print(f"average height = {totalSum}")


#---------------------#

#some examples that I found for summing with a for loop 


# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("The given list is:")
# print(myList)
# sumOfElements = 0
# for element in myList:
#     sumOfElements = sumOfElements + element

# print("Sum of all the elements in the list is:", sumOfElements)



# to find the length of the list to specify the length at the nth term, and do n-1.

# counter = 0
# for item in list:
#   counter += 1
#   print(counter)



  #another example 
#   inp_lst = ['Python', 'Java', 'Ruby', 'JavaScript']
# size = 0
# for x in inp_lst:
#     size += 1
# print(size)