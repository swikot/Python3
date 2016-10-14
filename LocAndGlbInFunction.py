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







