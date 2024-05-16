#Password Generator Project
import random
import string


lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digit_case = string.digits
marks_case = string.punctuation
print_case = string.printable

print (lower_case+upper_case+digit_case+marks_case+print_case)

grand_total = lower_case+upper_case+digit_case+marks_case

print (type(lower_case))

char_list2 = [x for x in print_case]

char_list = print_case.split()
print(char_list2)

char_list3 = list(map(str, grand_total))
print(char_list3)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P



#---------#

#ok so I got a really cool way of iterating a module into a list and one really nice feature that I will hold onto later 