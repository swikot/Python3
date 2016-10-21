__author__ = 'snow'

class Robot:
    pass


if __name__=="__main__":
    x = Robot()
    Robot.brand = "Kuka"
    print(x.brand)

    x.brand = "Thales"
    print("x ",x.brand)
    print(Robot.brand)

    y = Robot()
    print(y.brand)

    Robot.brand = "Thales"
    print(y.brand)

    print(x.brand)
    print(x.__dict__)
    print(y.__dict__)
    print(Robot.__dict__)
    y.brand="swikot"
    print(y.brand)
    print(y.__dict__)
    print(getattr(x,"enery",100))
