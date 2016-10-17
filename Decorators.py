__author__ = 'swikot'

def succ(first,*l):
    print("sum of the list is: ",(first+sum(l)))

list=[1,2,3,4,6,7]

successor=succ

# now
successor(*list)
succ(*list)
# The next important fact is that we can delete either "succ" or "successor" without deleting the function itself
# del succ
# successor(*list)


# Functions inside Functions
# The concept of having or defining functions inside of a function is completely new to C or C++ programmers:

print()
def f():
    def g():
        print("hello G ")

    print("hello F")
    g()
f()


# nsted function with proper return statement

def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5

    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!"
    return result

print(temperature(20))

# Functions as Parameters

print()
def g1():
    print("Hi i am g")

def f1(para):
    print("hi i am f")
    print("calling g1 now")
    print("para is my name but my real name is : ",para.__name__)
    para()

f1(g1)
print()
# another example
import math

def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1, 2, 2.5]:
        res += func(x)
    return res

print(foo(math.sin))
print(foo(math.cos))


# Functions returning Functions

def f2(x):
    def g2(y):
        return x+y+1
    return g2

nf1=f2(1)
nf2=f2(3)

print("fitst nf call gives us= ",nf1(1))
print("second nf call gives us= ",nf2(2))

print()
print()
# simple decoration
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration:")
foo("Hi")

print("We now decorate foo with f:")
foo = our_decorator(foo)

print("We call foo after decoration:")
foo(42)















