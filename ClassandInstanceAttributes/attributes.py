__author__ = 'snow'

class A:
    a="Hi all"


x=A()
print(x.a)
y=A()
print(y.a)
print(A.a)
x.a="hi adam"
print(x.a)
print(y.a)
A.a="Hi adam!!!"
print(x.a)
print(y.a)

print(x.__dict__)
print(y.__dict__)
print(A.__dict__)
print(x.__class__.__dict__)









