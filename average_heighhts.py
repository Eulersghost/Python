# Input a Python list of student heights
student_heights = input().split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇


#first 

#1. grab the length of the list and convert to an int


print(type(student_heights))

len_int_convert = int(len(student_heights))


#2. convert the list to a string -> integer

test_student_convert = int(str(student_heights))
print(test_student_convert)
# student_convert = int(''.join(map(str, student_heights)))

# print(student_convert, type(student_convert))


#Example code

# my_list = [1, 2, 3, 4, 5]
# int_result = int(''.join(map(str, my_list)))
# print("Result:", int_result)