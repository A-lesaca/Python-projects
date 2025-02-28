# This is a calculator
import math

operator=input("Please enter an operator (+ - * / **) :")
num1=float(input("Please enter first number:"))
num2=float(input("Please enter second number:"))

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
elif operator=="**":
    print(round(num1**num2,3))
else:
    print("Invalid operator")



