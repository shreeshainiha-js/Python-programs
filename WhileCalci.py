def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {"1": add, "2": subtract, "3": multiply,"4": divide} #call the corresponding functions if the respective characters entered.

while True:
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "5": #To end the loop
        print("Exiting calculator. Goodbye!")
        break
    if choice in operations: #check if any option given between 1-4.
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = operations[choice](num1, num2)
        print("Result:",result)
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")



"""Output:-

Simple Calculator
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter your choice (1-5): 1
Enter first number: 23
Enter second number: 34
Result: 57.0

Simple Calculator
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter your choice (1-5): 2
Enter first number: 134
Enter second number: 23
Result: 111.0

Simple Calculator
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter your choice (1-5): 3
Enter first number: 234
Enter second number: 3
Result: 702.0

Simple Calculator
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter your choice (1-5): 4
Enter first number: 23
Enter second number: 3
Result: 7.666666666666667

Simple Calculator
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter your choice (1-5): 5
Exiting calculator. Goodbye!
"""

