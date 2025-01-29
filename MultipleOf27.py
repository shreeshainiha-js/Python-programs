def multiple_of_27(number):
    if num%27==0: #check if the remainder should be zero.
        print(num, " is a multiple of 27")
    else:
        print(num,"is not a multiple of 27")

num=int(input("Enter the number:"))
multiple_of_27(num)


""" Output:
Enter the number:34
34 is not a multiple of 27

Enter the number:54
54  is a multiple of 27"""
