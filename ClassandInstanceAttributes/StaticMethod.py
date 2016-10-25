__author__ = 'swikot'

# class Robot:
#     __counter = 0
#
#     def __init__(self):
#         type(self).__counter += 1
#
#     def RobotInstances(self):
#         return Robot.__counter
#
#
# if __name__ == "__main__":
#     x = Robot()
#     print(x.RobotInstances())
#     y = Robot()
#     print(x.RobotInstances())
#     Robot.RobotInstances()



class Robot:
    __counter=0
    def __init__(self):
        type(self).__counter+=1

    @staticmethod
    def RobotInstance():
        return Robot.__counter



if __name__=="__main__":
    print(Robot.RobotInstance())
    x=Robot()
    print(x.RobotInstance())
    y=Robot()
    print(y.RobotInstance())
    print(Robot.RobotInstance())








