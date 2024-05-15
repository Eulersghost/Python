#looks like this exercise is replicating the max function 


#sample text from the lesson 
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])


#set counter 
score_counter = 0


#set the loop 
for x in student_scores:
	if x > score_counter:
		score_counter = x

print(f"The highest score in the class is: {score_counter}")
