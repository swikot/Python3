__author__ = 'snow'


# if contditon:
#     something
#     something
#     something


# nationality=input("Nationality?: ")

# if nationality=="french" or nationality=="French":
#     print(True)
#
#
# if nationality=="italian" or nationality=="Italian":
#     print(True)
#
# else:
#     print(False)


nationality="french"
if nationality=="french" or nationality=="French":
    print(True)


elif nationality=="italian" or nationality=="Italian":
    print(True)

else:
    print("you are neither French or Italian")


# General form of pythom if elif else

# if condition_1:
#     statement_block_1
# elif condition_2:
#     statement_block_2
#
# ...
#
# elif another_condition:
#     another_statement_block
# else:
#     else_block





# Example: Dog Years

age=eval(input("Dog age?:\n"))

if age<1:
     print("This can hardly be true!")

elif age==1:
    print("about 14 human years ! ")

elif age==2:
    print("about 22 human years ! ")

elif age>2:
    human=22+(age-2)*5
    print("Human years = ",human)

# True or False

# Unfortunately it is not as easy in real life as it is in Python to differentiate between true and false:
# The following objects are evaluated by Python as False:
#
# numerical zero values (0, 0L, 0.0, 0.0+0.0j),
# the Boolean value False,
# empty strings,
# empty lists and empty tuples,
# empty dictionaries.
# plus the special value None.
# All other values are considered to be True.


# The ternary if

a=2
b=1

if a>b:
    max=a
else:
    max=b


print("The max is =: ",max)


# now we will see the equivalent

max=a if(a>b) else b
print("result of ternary max is= ",max)

# But the ternary if statement is more than an abbreviation.
# It is an expression, which can be used within another expression:

max1=(a if(a>b) else b)*5

print("after using expression: ",max1)





# making large statement as a line

print()

a=2
b=3
c=10

if a>b and a>c:
    max2=a

elif b>a and b>c:
    max2=b

else:
    max2=c

print("The maximum number  of code snipet is : ",max2)


# another way to write this
# """
# x = float(input("1st Number: "))
# y = float(input("2nd Number: "))
# z = float(input("3rd Number: "))
#
# if x > y:
#     if x > z:
#         maximum = x
#     else:
#         maximum = z
# else:
#     if y > z:
#         maximum = y
#     else:
#         maximum = z
#
# print("The maximal value is: " + str(maximum)
# """

# making this snippet in one line


# x = float(input("1st Number: "))
# y = float(input("2nd Number: "))
# z = float(input("3rd Number: "))

print("maximum_val= ",max((2,3,4)))












