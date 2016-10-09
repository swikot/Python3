import time

__author__ = 'snow'

# pop and append

stack=[1,2,3,4,5,6]
stack.append(7) #append can be denoted as push/insert

print(stack)

stack.pop(-1)  #pop can be denoted as remove

print(stack)

stack.pop()

print(stack)

stack.pop()

print(stack)

# stack=stack.append(7)
# print(stack)
#
# print(stack)



# extends in list manipulation

list1=[1,2,3,4]
list2=[5,6]

list1.append(list2)
print(list1)
# for removing this extends is come

list3=[1,2,3,4]
list4=[5,6]
list3.extend(list4)
print(list3)

# extends for string and Tuples

names1=["a","b","c","d"]
names2="efgh"
names1.extend(names2)
print(names1)

names3=["asif","arif","khan"]
names4=("swikot","rishat","rakib")

names3.extend(names4)
print(names3)


# Combining with + operator


# Even though we get the same result, it is not an alternative to 'append' and 'extend':

age1=[1,2,3,4,5]
age2=[66,7,8,9,0]


print(age1+age2)


# never do the following

age3=[1,2,3]
age3=age3+[1,2,3]
print(age3)

# using remove on a list
#it removes a data without knowing the position

# maybe using linear search it finds the data and remove it
demo_list=[1,2,3,4,5,6,9,7]
demo_list.remove(7)
print("Printing demo List =",demo_list)


# Find the Position of an Element in a List index()

# problem here

print(demo_list.index(4))


# Using Insert()

Listing_quote=["I","He","like ","you"]
Listing_quote.insert(1,"and")
print("Total Listing quote: ",Listing_quote)


#Append can be simulated with insert()

Listing_quote.insert(len(Listing_quote),"very_much")
print("Total Listing quote: ",Listing_quote)

Listing_quote.insert(-1,"!")
print("Total Listing quote: ",Listing_quote)



















