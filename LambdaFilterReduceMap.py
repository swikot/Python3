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




