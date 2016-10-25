__author__ = 'snow'

# class A:
#     pass
#
#
# a=A()
# print(repr(a))
# print(str(a))

# class A:
#
#     def __repr__(self):
#         return "43"
#
#
# a=A()
# print(str(a))
# print(repr(a))


# o == eval(repr(o))

#
# This is shown in the following interactive Python session:
# >>> l = [3,8,9]
# >>> s = repr(l)
# >>> s
# '[3, 8, 9]'
# >>> l == eval(s)
# True
# >>> l == eval(str(l))
# True
# >>>
#
#
#
# >> import datetime
# >>> today = datetime.datetime.now()
# >>> str_s = str(today)
# >>> eval(str_s)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<string>", line 1
#     2014-01-26 17:35:39.215144
#           ^
# SyntaxError: invalid token
# >>> repr_s = repr(today)
# >>> t = eval(repr_s)
# >>> type(t)
# <class 'datetime.datetime'>
# >>>

# class Robot:
#     def __init__(self,name,build_year):
#         self.name=name
#         self.build_year=build_year
#
#     def __repr__(self):
#         return "Robot('" + self.name + "', " +  str(self.build_year) +  ")"
#
# if __name__=="__main__":
#     x=Robot("marvin longfello",1839)
#     x_str=str(x)
#     print(x_str)
#     print("Type of x_str is: ",type(x_str))
#     p=eval(x_str)
#     print("type of p is : ",p)

class Robot:
    def __init__(self,name,build_year):
        self.name=name
        self.build_year=build_year

    def __repr__(self):

        return "Robot(\"" + self.name + "\"," +  str(self.build_year) +  ")"

    def __str__(self):
        return "name: "+self.name+"   build year: "+str(self.build_year)



if __name__=="__main__":
    x=Robot("Marvin",1839)
    x_repr=repr(x)
    print(x_repr," ",type(x_repr))
    new = eval(x_repr)
    print(new," ",type(new))




















