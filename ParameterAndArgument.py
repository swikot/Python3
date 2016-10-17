__author__ = 'snow'

def function(x):
     print("x=: ",x,"  id=: ",id(x))
     x=42
     print("x=: ",x,"  id=: ",id(x))




p=6
print("value of p is = : ",p)
function(p)


print("now the value of p is: ",p)


def varpara(*x):
    print(x)


varpara(34,34,45)





# * function call

def func(x,y,z):
    print(x,y,z)


p=(10,20,30)
q=(11,2,3)
func(*p)
func(q[0],q[1],q[2])

# Arbitrary Keyword Parameters

def f(**args):
    print(args)


f(de="Germnan",en="English",fr="French")


# Double Asterisk in Function Calls


def variable(a,b,x,y):
    print(a,b,x,y)



d = {'a':'append', 'b':'block','x':'extract','y':'yes'}


variable(**d)

# combination can posiible

# def ()
#
# t = (47,11)
# d = {'x':'extract','y':'yes'}
# fac(*t, **d)

























