__author__ = 'snow'

# Python provides for six sequence (or sequential) data types:
# strings
# byte sequences
# byte arrays
# lists
# tuples
# range objects

# The items or elements of strings, lists and tuples are ordered in a defined sequence
# The elements can be accessed via indices

# accessing into a string

string="hello world"

print(string[0]," ",string[-1])



# a list is an collection of objects.
# accssing into List

List=["australia","england","spain","italy","bangladesh"]
print(List[0]," ",List[-1])
print(len(List))
fib=[1,2,3,4,5,6,7,8,9,10]
print(len(fib))


# BYTES
# small integer



# The main properties of Python lists:
# They are ordered
# The contain arbitrary objects
# Elements of a list can be accessed by an index
# They are arbitrarily nestable, i.e. they can contain other lists as sublists
# Variable size
# They are mutable, i.e. the elements of a list can be changed ***



# A list of mixed data types

mixed_data=[1,"2",5.6,"how are you?"]


# sublists or nested lists


persons=[["swikot","sakib"],["jobbar","motin",17],"funnyman"]


print(persons[0]," ",persons[1]," ",persons[2])

print(persons[0][0]," ",persons[0][1]," ",persons[1][0],persons[1][1]," ",persons[1][2]," ",persons[-1])
print(persons[-3][-2])

# complex or deeply nested Lists


complex_list = [["a",["b",["c","x"]]]]
print(complex_list[0])
print(complex_list[0][0]," ",complex_list[0][1])
print(complex_list[0][1][0]," ",complex_list[0][1][1])
print(complex_list[0][1][1][0]," ",complex_list[0][1][1][1])

# Tuples (immutable)

# A tuple is an immutable list, i.e. a tuple cannot be changed in any way once it has been created


# Where is the benefit of tuples?
# Tuples are faster than lists.
# If you know that some data doesn't have to be changed, you should use tuples instead of ' \
# 'lists, because this protects ' \
# 'your data against accidental changes.
# The main advantage of tuples consists in the fact that tuples can be used as keys in dictionaries, while lists can't.



Tuples=("tuples","are","immutable")
print(Tuples[0]," ",Tuples[1]," ",Tuples[2])
print(len(Tuples))


# Slicing technique (starting_point:number_of_slicing_elements)

text="It'sarainy day"
print(text)
first_six=text[0:6]
print(first_six)
start_four=text[5:]

print(start_four)

print(text[:])

without_last_five=text[0:-5]

print(without_last_five)


# Applying on a list

cities = ["Vienna", "London", "Paris", "Berlin", "Zurich", "Hamburg"]
print(cities[0:3])
print(cities[:3])
print(cities[:-3])

# slice(begin:end:step)


variable_text="Python was invented in denmark"
print(variable_text[::3])

variable_text2='Toronto is the largest City in Canada'
print(variable_text2[::3])
print(variable_text2[1::3])


#  length

array=[["integer","float"],["double","byte"],"string"]
print(len(array))
print(len(array[0]))
print(len(array[2]))


#Concatenation of Sequences


# string concatanation
first_name="Matt"
last_name="damon"
con_string=first_name+" "+last_name
print(con_string)

#Lists conctanation

colours1 = ["red", "green","blue"]
colours2 = ["black", "white"]

con_list=colours1+colours2


print(con_list)
colours1+=colours2
print(colours1)



# element in somewhere



in_string="matt" in con_string
in_list="black" in con_list
print(in_string)
print(in_list)


# repetation


repetation=["1","2","3"]*3
print(repetation)

num_repetation_failed=[1,2,3]*3
print(num_repetation_failed)



# The Pitfalls of Repetitions

x=['a','b','c']
y=[x]*3

print(y)

y[0][0]="p"

print(y)



# persons=[["swikot","sakib"],["jobbar","motin",17],"funnyman"]

persons[0][0]="asif"
print(persons)

































