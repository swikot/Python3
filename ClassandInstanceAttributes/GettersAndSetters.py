__author__ = 'snow'

# class A:
#
#
#     def __init__(self,x):
#         self.__x=x
#
#     def getX(self):
#         return self.__x
#     def setX(self,x):
#         self.__x=x
#
#
# p1=A(42)
# p2=A(4221)
#
# print(p1.getX())
#
# p1.setX(22)
# print(p1.getX()+p2.getX())
# p1.setX(p1.getX()+p2.getX())
# print(p1.getX())
#
# #if attributes are public then we can write this as  p1.x = p1.x + p2.x
#
# class B:
#     def __init__(self,x):
#         self.x=x
#
#     def getX(self):
#         return self.x
#     def setX(self,x):
#         self.x=x
#
#
# q1=B(10)
# q2=B(20)
#
# print(q1.getX())
# print(q2.getX())
# print("........")
# q1.x=q1.x+q2.x
# print(q1.getX())




class P:
    def __init__(self,x):
        self.setX(x)

    def getX(self):
        return self.__x
    def setX(self,x):
        if x <0:
            self.__x=0
        elif x>1000:
            self.__x=1000
        else:
            self.__x=x


p1 = P(1001)
print(p1.getX())

p2 = P(15)
print(p2.getX())

p3 = P(-1)
print(p3.getX())

























