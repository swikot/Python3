__author__ = 'snow'




# We have the same classification again in object-oriented programming:
#
#
#
# 1.Private attributes should only be used by the owner,
# i.e. inside of the class definition itself.
# 2.Protected (restricted) Attributes may be used, but at your own risk.
# Essentially, this means that they should only be used under certain conditions.
# 3.Public Attributes can and should be freely used.


# class A():
#     def __init__(self):
#         self.pub="I am private"
#         self._prot="I am protected"
#         self.__priv="I am private"
#
#
# x=A()
# print(x.pub)
# x.pub=x.pub+" and I am changable"
# print(x.pub)
#
# print(x.__priv) #no attribute error

# class Robot:
#     def __init__(self,name,build_year):
#         self.__name=name
#         self.__build_year=build_year
#
#     def say_Hi(self):
#         if self.__name:
#             print("hi i am : ",self.__name)
#         else:
#             print("I am a robot without a name")
#
#
#     def set_name(self,name):
#         self.__name=name
#     def get_name(self):
#         return self.__name
#     def set_buld_year(self,build_year):
#         self.__build_year=build_year
#     def get_build_year(self):
#         return self.__build_year
#
#     def __repr__(self):
#         return "Robot('" + self.__name + "', " +  str(self.__build_year) +  ")"
#
#     def __str__(self):
#         return "Name: " + self.__name + ", Build Year: " +  str(self.__build_year)
#
#
#
# if __name__=="__main__":
#     x=Robot("Marvin Longfelo",1839)
#     y=Robot("Jack Daniyels",1739)
#
#     for rob in [x,y]:
#         rob.say_Hi()
#         if rob.get_name()=="Jack Daniyels":
#             rob.set_buld_year(1939)
#         print("I was built in the year " + str(rob.get_build_year()) + "!")
#

#
# class A():
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def GetX(self):
#         return self.__x
#
#     def GetY(self):
#         return self.__y
#
#     def SetX(self, x):
#         self.__x = x
#
#     def SetY(self, y):
#         self.__y = y
























































