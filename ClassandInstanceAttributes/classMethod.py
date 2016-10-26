__author__ = 'snow'


class A(object):
    __counter=0
    def __init__(self):
        type(self).__counter+=1

    @classmethod
    def Ainstance(cls):
        return cls,A.__counter



if __name__=="__main__":
    print(A.Ainstance())
    x=A()
    print(x.Ainstance())
    y=A()
    print(y.Ainstance())
    print(A.Ainstance())
