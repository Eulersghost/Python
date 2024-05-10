# Input a Python list of student heights
student_heights = input().split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇


#1. grab the length of the list and convert to an int

len_int_convert = int(len(student_heights))


#2. convert the input list to a integer

studentSum = int(sum(student_heights))


#3. average the results together

totalSum = studentSum / len_int_convert
∏

print(f"total height = {studentSum}")
print(f"number of students = {len_int_convert}")
print(f"average height = {studentSum}")



# test_student_convert = int(str(student_heights))
# print(test_student_convert)
# student_convert = int(''.join(map(str, student_heights)))

# print(student_convert, type(student_convert))


#Example code

# my_list = [1, 2, 3, 4, 5]
# int_result = int(''.join(map(str, my_list)))
# print("Result:", int_result)