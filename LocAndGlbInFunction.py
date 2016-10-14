__author__ = 'Swikot'


#1. This will print python
print("--1st Case--")
def f():
    print(s)

s="python"
f()
print()
# 2.This will also print python and java


print("--2nd Case--")
def f1():
    s="java"
    print(s)

s="python"
f1()
print(s)
print()

# 3.this will show errors
# print("--3rd Case--")
# def f2():
#     print(s)
#     s="java"
#     print(s)
#
# s="python"
# f2()
# print(s)
print()
print("--4th Case--")
def f3():
    global s
    print(s)
    s="java"
    print(s)

s="python"
f3()
print(s)
print()

# Arbitrary Number of Parameters

def arithmetic_mean(first, *values):

    return ((first + sum(values)) / (1+len(values)))


print("arithmetic mean is :",arithmetic_mean(45,32,89,78))
print("arithmetic mean is :",arithmetic_mean(8989.8,78787.78,3453,78778.73))
print("arithmetic mean is :",arithmetic_mean(45,32))
print("arithmetic mean is :",arithmetic_mean(45))


print()


# using * for List
my_list = [('a', 232),
           ('b', 343),
           ('c', 543),
           ('d', 23)]

# this list must be written as [('a', 'b', 'c', 'd'),(232, 343, 543, 23)]

# p=[1,2,3]
# q=[4,5,6]
# list1=list(zip(p,q))
# print(list1)


print("list : ",list(zip(*my_list)))


# Arbitrary Number of Keyword Parameters


def keyword_function(**keywords):
    return keywords



j=keyword_function(a="bangladesh",b="india",c="chaina",d="korea")

print("Final Value is : ",j)


# another approach is
# >>> def f(a,b,x,y):
# ...     print(a,b,x,y)
# …
# >>> d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
# >>> f(**d)
# ('append', 'block', 'extract', 'yes')















































