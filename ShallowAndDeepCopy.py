__author__ = 'snow'

# Shallow and deep copying starts
x = 3
y = x   #y points the same memory location of y
print(id(x), id(y))
y = 4
print(id(x), id(y))
print(x,y)

print("\n")

# Copying a List
colours1=["red","blue"] # no sublists are contained in the list is known as shallow List

colours2=colours1

print(colours2)
print("id of colours1=",id(colours1)," and id of colours2=",id(colours2))

colours2=["white","yellow"]
print()

print(colours1)
print(colours2)

print("id= ",id(colours1),"  id= ",id(colours2))


# what happens if we change any of the (colours3 and colours4)

colours3=["green","red"]

colours4=colours3

print(id(colours3)," ",id(colours4))

colours4[1]= "yellow"
print(colours3)
print(colours4)

print(id(colours3)," and ",id(colours4))

# id changing

colours5=["green","yellow"]
colours6=["green","yellow"]

print(id(colours5)," and ",id(colours6)) #here id will change



# Copy a shallow list with Slicing Operator where they will not share same list

list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1[:]

# initial Print statement
print("list1= ",list1)
print("list2= ",list2)

# change in list2
list2[1]=11
# now prints the changed list

print("Changed list1= ",list1)
print("Changed list2= ",list2)


# Difficulty arises for nested list by slicing

list3=["a","b",["c","d"]]
list4=list3[:]
print(list4)


print(id(list3)," ",id(list4))


list4[0]="i"
list4[1]="j"

print("Printing list3= ",list3)
print("Printing list4= ",list4)

# slicing not applicable case


list4[2][1]="f"
print()

print("Now list3 output= ",list3)
print("Now list4 output= ",list4)



# using method deepcopy instead of










