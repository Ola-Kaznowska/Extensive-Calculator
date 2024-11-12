from Addition import Addition
from Subtraction import Subtraction
from Multiplication import Multiplication
from Division import Division
while True:
    
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    user = int(input("Choose an operation (1/2/3/4): "))
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    if user == 1:
        print(f"{a} + {b} = {Addition(a,b)}")
    elif user == 2:
        print(f"{a} - {b} = {Subtraction(a,b)}")
    elif user == 3:
        print(f"{a} * {b} = {Multiplication(a,b)}")
    elif user == 4:
        print(f"{a} / {b} = {Division(a,b)}")