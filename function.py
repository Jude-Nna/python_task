#function: is an unit of code that perform something. A funtion is an action.# # custom function sample to add
# def add_numbers(a, b):
#     return a + b
 
# # another without return statement
# def add_numbers_no_return(a, b):
#     print(a + b)
 
# result1 = add_numbers(3, 5)
# result2 = add_numbers_no_return(3, 5)
 
# print("result1 is:", result1)  # This will print: result1 is: 8
# print("result2 is:", result2)  # This will print: result2 is:
 
 
# create a program that takes three numbers, multiplies the first two,
# and then adds the third number to the result.
# The program should then print the final result.
 
 
 
from lib import multiply, add
 
 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
 
mul = multiply(num1, num2)
 
final_result = add(mul, num3)
 
print("The final result is:", final_result)
 