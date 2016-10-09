from copy import deepcopy

list1=[1,2,3,[4,5]]
list2=deepcopy(list1)

print("deepcopied list1= ",list1)
print("deepcopied list2= ",list2)

# its time to change list2

list2[3][0]=7
list2[3][1]=8

print()
print("After changing list1: ",list1)
print("After changing list2: ",list2)

