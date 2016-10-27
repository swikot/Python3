__author__ = 'snow'

def successor(number):
    return number+1


print(successor(1))
print(successor(1.6))

# conventional C++ and java will not work here

# print()
# def f(n):
#     return n+42
# def f(n,m):
#     return n+m+43
#
#
# print("function values: ",f(4,3))

# if we want to simulate this this behaviour thn we can write as

def function(n,m=None):
    if m:
        return n+m+1
    else:
        return n+1

print("values: ",function(10))
print("values: ",function(10,20))

# another alter

def function_ov(*x):
    if len(x)==1:
        return x[0]+1
    else:
        return x[0]+x[1]+1

print("final values: ",function_ov(10))
print("final values: ",function_ov(10,20))


















