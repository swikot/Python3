__author__ = 'snow'

# Data Abstraction = Data Encapsulation+Data Hiding


# class Robot:
#     def __init__(self,name=None):
#         self.name=name
#     def say_hi(self):
#         if self.name:
#             print("my name is: ",self.name)
#         else:
#             print("I am a Robot without a name")
#
#     def get_Name(self):
#         return self.name
#     def set_Name(self,name):
#         self.name=name
#
#
# if __name__=="__main__":
#     x=Robot()
#     x.set_Name("Henry")
#     x.say_hi()
#     y=Robot()
#     y.set_Name(x.get_Name())
#     print(x.get_Name())



class Robot:

    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_build_year(self, by):
        self.build_year = by

    def get_build_year(self):
        return self.build_year


x = Robot("Henry", 2008)
y = Robot()
y.set_name(x.get_name())
print(x.get_name(), x.get_build_year())