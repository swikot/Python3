__author__ = 'snow'
#
# class P:
#     def __init__(self,x):
#         self.x=x
#
#     @property
#     def x(self):
#         return self.__x
#
#
#     @x.setter
#     def x(self,x):
#         if x>1000:
#             self.__x=1000
#         elif x<0:
#             self.__x=0
#         else:
#             self.__x=x
#
#
#
# a=P(1001)
# print(a.x)
# a.x=-12
# print(a.x)
# a.x=12
# print(a.x)
#



# class P:
#
#     def __init__(self,x):
#         self.setX(x)
#
#     def getX(self):
#         return self.__x
#
#     def setX(self, x):
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x
#
#     x = property(getX, setX)







class OurClass:

    def __init__(self, a):
        self.OurAtt = a

    @property
    def OurAtt(self):
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val


x = OurClass(10)
print(x.OurAtt)






x = OurClass(-1)
print(x.OurAtt)


