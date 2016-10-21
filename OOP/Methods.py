__author__ = 'snow'


def hi(obj):
    print("hi i am ",obj.name)



class Robot:
    say_hi=hi


x=Robot()
x.name="maverick"
hi(x)
Robot.say_hi(x)

#
# The proper way to do it:
# Instead of defining a function outside of a class definition and
# binding it to a class attribute, we define a method directly inside (indented) of a class definition.
# A method is "just" a function which is defined inside of a class.
# The first parameter is used a reference to the calling instance.
# This parameter is usually called self.
# Self corresponds to the Robot object x.


# We have seen that a method differs from a function only in two aspects:
# It belongs to a class, and it is defined within a class
# The first parameter in the definition of a method has to be a
# reference to the instance, which called the method.
#  This parameter is usually called "self".

print(" ")
























