__author__ = ''

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








































