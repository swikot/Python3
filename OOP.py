__author__ = 'swikot'

# features of OOP
# object-oriented programming: Library of the Court of Appeal for Ontario in Toronto
#
# Encapsulation
# Data Abstraction
# Polymorphism
# Inheritance

class Robot:

    pass

if __name__== "__main__":
    x=Robot()
    y=Robot()
    y2=y
    print(x==y," ",id(x)," ",id(y))
    print(y==y2," ",id(y)," ",id(y2))
    x.name = "Marvin"
    x.build_year = "1979"
    y.name = "Caliban"
    y.build_year = "1993"
    print()
    print(x.name," ",y.name)
    print(x.build_year," ",y.build_year)
    print()
    print(x.__dict__)
    print(y.__dict__)



