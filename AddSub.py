def Add_Sub(num1,num2):
    addResult=num1+num2
    subResult=num1-num2
    #Use abs() function to return absolute value (It removes the negative sign).
    print("The addition of ",num1 ,"and", num2 ,"is",abs(addResult)) 
    print("The subtraction of ",num1 ,"and", num2 ,"is",abs(subResult))

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
Add_Sub(num1,num2)


 """Output:
Enter the first number:34
Enter the second number:24
The addition of  34 and 24 is 58
The subtraction of  34 and 24 is 10

Enter the first number:45
Enter the second number:-5
The addition of  45 and -5 is 40
The subtraction of  45 and -5 is 50
"""
