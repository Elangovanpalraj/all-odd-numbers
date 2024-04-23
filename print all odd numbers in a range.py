# Python program to print all odd numbers in a range
# ------------------------------------------------\n
'''
Input: start = 4, end = 15
Output: 5, 7, 9, 11, 13, 15

Input: start = 3, end = 11
Output: 3, 5, 7, 9, 11
'''
# list using for loop
# -------------------\n
# Python program to print odd Numbers in given range
 
start, end = 4, 19
 
# iterating each number in list
for num in range(start, end + 1):
     
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")

print(' ')
# Example #2: Taking range limit from user input
# ----------------------------------------------\n
# Python program to print Even Numbers in given range
 
start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))
 
# iterating each number in list
for num in range(start, end + 1):
 
    # checking condition
    if num % 2 != 0:
        print(num)

print(' ')
# Example #3
# ----------\n
# Uncomment the below two lines for taking the User Inputs
#start = int(input("Enter the start of range: "))
#end = int(input("Enter the end of range: "))
 
# Range declaration
start = 5
end = 20
 
if start % 2 != 0:
 
    for num in range(start, end + 1, 2):
        print(num, end=" ")
else:
 
    for num in range(start+1, end + 1, 2):
        print(num, end=" ")


print(' ')

# Example #4: Taking range limit from user input
# ----------------------------------------------\n

# Python program to print Even Numbers in given range
 
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
 
#create a list that contains only Even numbers in given range
even_list = range(start, end + 1)[start%2::2]
 
for num in even_list:
    print(num, end = " ")

print(' ')
# Method: Using the lambda function
# ----------------------------------\n
# Python code To print all odd numbers 
# in a given range using the lambda function
a=3;b=11
li=[]
for i in range(a,b+1):
    li.append(i)
# printing odd numbers using the lambda function
odd_num = list(filter(lambda x: (x%2!=0),li))  
print(odd_num)
print(' ')
# Method: Using recursion
# ------------------------\n
def odd(num1,num2):
    if num1>num2:
        return
    if num1&1:
      print(num1,end=" ")
      return odd(num1+2,num2)
    else:
      return odd(num1+1,num2)
num1=5;num2=15
odd(num1,num2)
print(' ')

# Method: Using list comprehension
# --------------------------------
x = [i for i in range(4,15+1) if i%2!=0]
print(*x)
print(' ')
# Method: Using pass
# -----------------\n
a=4;b=15
for i in range(a,b+1):
  if i%2==0:
    pass
  else:
    print(i,end=" ")
print(' ')
# Method: Using filter method:
# --------------------------\n
# Python program to print Even Numbers in given range
  
# Range declaration
a=4;
b=15;
 
#create a list that contains only Even numbers in given range
l= filter(lambda a : a%2 , range(a, b+1))
print(*l)
print(' ')
# Method: Using bitwise & operator
# --------------------------------\n
# Python program to print odd Numbers in given range
#using bitwise & operator
  
 
start, end = 4, 19
 
  
 
# iterating each number in list
 
for num in range(start, end + 1):
 
      
 
    # checking condition
 
    if num & 1 != 0:
 
        print(num, end = " ")
 
 #this code is contributed  by vinay pinjala.
print(' ')
# Method: Using bitwise | operator
# -------------------------------\n
# Python program to print odd Numbers in given range
#using bitwise | operator
  
 
start, end = 4, 19
 
  
 
# iterating each number in list
 
for num in range(start, end + 1):
 
      
 
    # checking condition
 
    if num | 1 == num:
 
        print(num, end = " ")
print(' ')
# Method : Using numpy module:
# --------------------------\n
import numpy as np
 
# Range declaration
a = 3
b = 15
 
# Create an array containing numbers in the range
arr = np.arange(a, b+1)
 
# Create a new array containing only even numbers
evens = arr[arr % 2 != 0]
 
# Print the array of even numbers
print(*evens)
#This code is contributed by Jyothi pinjala
print(' ')
# Method: Using continue keyword
# ------------------------------\n
a = 4
b = 15
for i in range(a, b+1):
    if i % 2 == 0:
        continue
    else:
        print(i, end=" ")
 
     # This Code is contributed by Pratik Gupta (guptapratik)

print(' ')
# Method: Using filterfalse method
# ------------------------------\n
# Python 3 code to demonstrate
# print odd number in range
import itertools
 
# Range declaration
a = 3
b = 15
 
# using filterfalse function 
evens = list(itertools.filterfalse(lambda x: x%2==0, range(a, b+1)))
 
# Print the array of even numbers
print(*evens)
print(' ')
#-------------------------------------------------------------\n































































































