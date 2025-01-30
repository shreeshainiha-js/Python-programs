num=int(input("Enter the number:"))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if(sum==num):
    print("The given number is a perfect number")
else:
    print("The given number is not a perfect number")


""" Output:
Enter the number:6
The given number is a perfect number

Enter the number:26
The given number is not a perfect number
"""
