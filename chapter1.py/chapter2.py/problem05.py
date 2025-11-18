#Write a python program to find an average of two numbers entered by the user.


a = int(input("Enter your first value:")) #as we know in input() function every value even no is string 
b = int(input("Enter your second value:")) #thats why we use int to convert string into float which give in answer always float value


print("The average of your value is:", (a+b/2))
print(type(a+b/2))
