import math

__author__ = 'snow'




edibles = ["ham","spam","eggs","nuts"]

for i in edibles:
    if i=="spam":
        print("no more spam")
        break
    print("delicious food ",i)

else:
    print("print me ")

print("wait for your call")
print()




# pithagorus theorem
fibonacci=[0,1,1,2,3,5,8,13]

for i in range(len(fibonacci)):
    print(fibonacci[i],end=" ")



print("\n")
for i in fibonacci:
    print(i,end=" ")

# List iteration with Side Effects

colours = ["red"]
for i in colours:
    if i == "red":
        colours += ["black"]
    if i == "black":
        colours += ["white"]
print(colours)



# using slicing operator It can be removed

colourss=["red"]
for i in colourss[:]:
    if i=="red":
        colourss+=["black"]
    if i=="black":
        colourss+="white"


print(colourss)















