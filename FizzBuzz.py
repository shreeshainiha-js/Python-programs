def FizzBuzz(num):
    result=[]
    for i in range(1,num+1):
        if i%3==0 and i%5==0: #check if divisible by both 3 and 5. Then append the string with that number.
            result.append("FizzBuzz")
        elif i%3==0: #check if divisible by 3. Then append the string with that number.
            result.append("Fizz")
        elif i%5==0: #check if divisible by 5. Then append the string with that number.
            result.append("Buzz")
        else: # otherwise print the number as it is.
            result.append(str(i))
    return result

nums=int(input("enter the number:"))
print(FizzBuzz(nums))


""" Output:
enter the number:15
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
"""
