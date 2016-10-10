__author__ = 'swikot'

# hi sets starting point

#  set contains an unordered collection of unique and immutable objects

# Sets


# If we want to create a set, we can call the built-in set function with a sequence or another iterable object:


x=set("my name is swikot")
print(x)
# {'w', 'i', 'o', 'y', 's', 'a', ' ', 'm', 'n', 'k', 't', 'e'}
print(type(x))


# Building set with lists




y=set(["java","pearl","python"])
print(y)
# {'java', 'pearl', 'python'}
# no list brackets


# immutable sets
# Sets are implemented in a way, which doesn't allow mutable objects
# we cannot include for example lists as elements:



cities = set((("Python","Perl"), ("Paris", "Berlin", "London")))

print(cities)
# cities = set((["Python","Perl"], ["Paris", "Berlin", "London"]))  prohabited



# Though sets can't contain mutable objects, sets are mutable:
city = set(["Frankfurt", "Basel","Freiburg"])
city.add("dhaka")
print(city)


# frozenset

# Frozensets are like sets except that they cannot be changed, i.e. they are immutable:

country=frozenset(["Frankfurt", "Basel","Freiburg"])
# country.add cant possible

# Improved notation
# We can define sets (since Python2.6) without using the built-in set function. We can use curly braces instead:
sets_books={"bangla","english","arabic"}

print(sets_books)

sets_books.add("mathmatics")  #perfacto
print(sets_books)



# set operations


# Add operations


# A method which adds an element, which has to be immutable, to a set.

colours = {"red","green"}

colours.add("yellow")
# colurs.add(["white","black"]) not possible
# coz they are mutable
# add only adds immutable values
print(colours)


# clear()

# all elements will be removed from set



sets_remove={"swikot","asif","hans","walton"}
print(sets_remove)

sets_remove.clear()

print(sets_remove)


# copy

# creats shallow copy

sets1={"roy","cook","butlar","dicket","morgan"}
sets2=sets1.copy()

print(sets1)
print(sets2)

sets2.clear()
print()
print("after clear sets1: ",sets1)
print("after clear sets2: ",sets2)

# Just in case, you might think, an assignment might be enough:

sets3={"mashrafi","sabbir","musfick","mahmudullah"}
sets4=sets3

print(sets3)
print(sets4)

sets4.clear()


print()

print(sets3)
print(sets4)





# difference()

# This method returns the difference of two or more sets as a new set.
x = {"a","b","c","d","e"}
y = {"b","c"}
z = {"c","d"}


print(x.difference(y))
print(x.difference(z))
print(y.difference(z))

print(x.difference(y).difference(z))


print(x-y)
print(x-z)
print(x-y-z)




# difference_update()
# same as x=x-y
x.difference_update(y)
print(x)
print(y)


# discard(el)

# An element el will be removed from the set, if it is contained in the set. If el is not a member of the set, nothing will be done.

sets_name={"montu","poltu","rahim","karim","ashik"}
sets_name.discard("montu")
print(sets_name)
sets_name.discard("karim")
print(sets_name)
sets_name.discard("ashik")
print(sets_name)

sets_name.discard("swikot")
print(sets_name)#no error occurs



# remove(el)
# works like discard(), but if el is not a member of the set, a KeyError will be raised.


sets_name2={"montu","poltu","rahim","karim","ashik"}
sets_name2.remove("montu")
print(sets_name2)
# sets_name2.remove("swikot")
# print(sets_name2)  not possible , cz  a key error will be raised


# intersection(s)
# Returns the intersection of the instance set and the set s as a new set
#  In other words: A set with all the elements which are contained in both sets is returned.
# mind it a new set will be created


pi1= {"a","b","c","d","e"}
pi2= {"c","d","e","f","g"}

new_intersection_set=pi1.intersection(pi2)
print("new intersection sets=",new_intersection_set)


print("Intersection point with and operator= ",pi1 & pi2)


# issubset()
# x.issubset(y) returns True, if x is a subset of y

name11= {"a","b","c","d","e"}
name12= {"c","d"}

print(name12.issubset(name11))
print(name12 > name11)
print(name12 <= name11)#equivalent to issubset()
print(name11 >= name12)





# issuperset()
# >= is equaivalent to issuperset

print("name 11 is the superset of name 12: ",name11.issuperset(name12))

print(name12 < name11)# name12  is  a proper subset

print(name12 > name11) #name11 is a proper superset




# pop
# pop() removes and returns an arbitrary set element. The method raises a KeyError if the set is empty

name11.pop()
print(name11)
name11.pop()
print(name11)

# end of set



































































































