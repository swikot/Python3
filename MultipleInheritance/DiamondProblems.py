__author__ = 'snow'


class A():
    def m(self):
        print("m in A is called")

class B(A):
    pass
#def m(self):
#     print("m in B is called")



class C(A):
    def m(self):
        print("m in C is called")
class D(B,C):
    pass

x=D()
x.m()


