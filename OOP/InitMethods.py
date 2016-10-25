class Robot:
    def __init__(self,name=None):
        self.name=name


    def say_hi(self):
        if self.name:
            print("I am Robot name:",self.name)
        else:
            print("I am Robot without a name")


if __name__=="__main__":
    x=Robot()
    x.say_hi()
    x=Robot("maverick")
    x.say_hi()











# Data Abstraction, Data Encapsulation, and Information Hiding















