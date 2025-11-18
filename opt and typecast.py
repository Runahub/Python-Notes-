# operators = symbol that performs a certain operation between operands
# types : 
#  1. Arithmetic operators: +, -, *, / etc.
# 2. Assignment operators: =, +=, -= etc.
# 3. Comparison operators: ==, >, >=, <, != etc.
# 4. Logical operators: and, or, not.

# Arithmetic operators
a = 45
b = 827
print(a + b)
print(a - b)
print(a * b)
print(a/b)



# Assignment operators 
num = 2004
# num assign the value 2004 = represent the assing operands
num = num + 500
print("num:", num)

num1 = 73
num1 -= 55 #decrement the value of num1 by 55and then assign it to num1
# for subt -=
print("num1:",num1)

num2 = 543
num2 += 500 # Increment the value of num2 by 500 and then assign it to num2
# for add +=
print("num2", num2)



# Comparison / relational operators
#  relational always give answer in TRUE/FALSE = Boolean data type

a1 = 55
b1 = 43
sum = a<b
print(sum)


a3 = 23.68
b3 = 82.02
sum =  a >= b
print(sum)

d = 5!=5
print("comparison of d :", d)

# relational always give answer in TRUE/FALSE = Boolean data type

a4 = 50
b4 = 20

print("comp1:",a==b)
print("comp2:",a!=b)
print("comp3:",a>=b)
print("comp4:",a<=b)
print("comp5:",a>b)
print("comp6:",a<b)


# logical operators = not , and , or
# work on boolean data type
# Not
# Note : if we take any boolean value then Not operators always return their opposite
a = 50
b = 30
print(not False)
print("Not operator:",not(a>b))



# And 
# work on 2 value
vol1 = True
vol2 = True
print("And operator:", vol1 and vol2)


# OR
# also work on 2 value
vol3 = True
vol4 = False
print("OR operatos:", vol3 or vol4)


e = True or False
# TRUTH TABLE OF "OR"
print("for OR operators TRUTH TABLE is:")
print("True or True is:", True or True)
print("True or False is:", True or False)
print("False or False is:",False or False)
print("False or True is:", False or True)




# TRUTH TABLE OF "AND"
print("for AND operators TRUTH TABLE is:")
print("True and True is:", True and True)
print("True and False is:", True and False)
print("False and False is:",False and False)
print("False and True is:", False and True)


#TRUTH TABLE OF "AND"
# return their opposite value
#  also work on single value

print(not(True))
print(not(False))




#  NEXTTTTTTTTTT
# TYPE() FUNCTION AND TYPECASTING
# type() function:used to find the data type of a given variable in python.


a = 31
b = "31"

print(type(a))
print(type(b))

# TYPECASTING -------------

# There are many functions to convert one data type into another.
# str(31) =>"31" # integer to string conversion
# int("32") => 32 # string to integer conversion
# float(32) => 32.0 # integer to float conversion



z = int("31") #z is str but it should be int
y = str(31)  #y is int  but type should be str
x = float(32) #x is int but it shold be float
print(type(z))
print(type(y))
print(type(x))


