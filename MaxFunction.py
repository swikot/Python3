__author__ = 'snow'

# x = eval(input("1st Number: "))
# y = eval(input("2nd Number: "))
# z = eval(input("3rd Number: "))
#
#
# maximum=max((x,y,z))
# mximum2=maximum
# print("maximum=" +str(maximum))
# print("maxumum2=",mximum2)
#

print()

number_of_values = int(input("How many values? "))

maximum = float(input("Value: "))
print(maximum)
for i in range(number_of_values - 1):
    value = float(input("Value: "))
    if value > maximum:
        maximum = value

print("The maximal value is: " + str(maximum))




