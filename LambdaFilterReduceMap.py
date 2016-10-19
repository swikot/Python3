__author__ = 'snow'
# lambda
# lambda argument_list: expression

sum=lambda x,y:x+y
print(sum(10,12.3))

# equivalent to
# def sum(x,y):
#      return x + y
#
# print(sum(3,4))
mx=lambda x,y:x if x>y else y
print("the max value is: ",mx(10,11))

# more about lambda

def value(n):
    return lambda x:x+n


f=value(42)

print("sum of f is: ",f(10))
print("sum of f is: ",f(20))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pairs:pairs[1])
print("print pairs: ",pairs)


# The map() Function
# the advantage of the lambda operator can be
# seen when it is used in combination with the map() function
# map() is a function which takes two arguments:
# r = map(func, seq)
print()
def fahrenheit(T):
     return ((float(9)/5)*T + 32)

def celsius(T):
     return (float(5)/9)*(T-32)

temperatures = (36.5, 37, 37.5, 38, 39)

F=map(fahrenheit,temperatures)
C=map(celsius,temperatures)

temp_in_far=list(map(fahrenheit,temperatures))
temp_in_cels=list(map(celsius,temperatures))
print("temp in far: ",temp_in_far)
print("temp in cels: ",temp_in_cels)


# we can do the same thing with lambda and map

F1=list(map(lambda x:(float(9)/5)*x + 32,temperatures))
print("the vale of f1 is: ",F1)
C1=list(map(lambda x:(float(5)/9)*(x-32),temperatures))
print("the value of C1 is: ",C1)
# some neat example
l=[1,2,3,4,5]
square=list(map(lambda x:x**2,l))
print("The square of the list l is: ",square)

# we can apply more than one sequence in map(func,nsequence)
l1=[10,20,30,40]
l2=[50,60,70,80]
l3=[90,10,20,30]

arith=list(map(lambda x,y,z:x+y-z,l1,l2,l3))

print("The value of arithmetic ops is: ",arith)
print()
# Filtering
# filter(function, sequence)
# filter out all the elements of a sequence
fibonacci = [0,1,1,2,3,5,8,13,21,34,55]

odd_numbers=list(filter(lambda x:x%2,fibonacci))
print("the odd numbers are: ",odd_numbers)
even_numbers=list(filter(lambda x:x%2==0,fibonacci))
print("the even numbers are: ",even_numbers)

# Reducing a List
# The function
# reduce(func, seq)






