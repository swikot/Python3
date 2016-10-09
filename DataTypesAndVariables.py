# __author__ = 'snow'
#
# i='string '
# y=i
#
# print("id of i is =",id(i))
#
# print("id of y is =",id(y))
#
# y=78
#
#
# print("now the id of y is =",id(y))
# # numbers
# x=hex(18)
# y=bin(18)
# z=oct(18)
# print("hexa decimal of 18 is =",x," type of x=",type(x))
# print("binary of 18 is =",y,"type of y=",type(y))
#
# print("octal of 18 is =",z,"type of z=",type(z))
#
# # complex number
#
# complex_number1=3+4j
# complex_number2=4+3j
#
# sum_of_complex_number=complex_number1+complex_number2
# print("complex number summation result",sum_of_complex_number,"type=",type(sum_of_complex_number))
#
# # integer division is resulting a floating point number
# integer_division_number1=10
# integer_division_number2=3
# integer_division_result=10/3
# integer_division_result2=10//3
# print("integer division result is =",integer_division_result,"type of integer_division",type(integer_division_result))
# print("integer division result is =",integer_division_result2,"type of integer_division2",type(integer_division_result2))
#
#
# # strings in Python 3
#
# string1='I like this wonderful world'
# string2="I like this wonderful world"
#
# # differences between '' and ""
#
# string3='I don\'t know'
# string4="I don't know"
# print(string3)
# print("."*10)
# print(string4)
#
#
# string5="He said that: \"you are a mad man\""
# print(string5)
#
# # example '''
#
# string6='''
# Hi i like this world
# but i don't about
# "world" 'policy'
#
# '''
#
# print(string6)


# Index of string

hello_world="Hello World"

print(hello_world[0]," and " , hello_world[len(hello_world)-1])
print(hello_world[-len(hello_world)], "and ",hello_world[-1])

# string operations

s1="hello world !"
s2="I like it"
concatanation=s1+s2
print("Concatanation operation result=",concatanation)
repetation=s1*4
print("Repetation operation result=",repetation)
indexing=s1[0]
print("Indexing operation result=",indexing)
slicing=s1[0:5]
print("Slicing operation result=",slicing)
length=len(slicing)
print("length of slicing =",length)

#immutable string
string="Hello!"
# string[-1]="."   not possible because its immutable
string="world!"  #assigning a completely new string object


# string peculiarity

a="Linux"
b="Linux"

print("id of a",id(a))
print("id of b",id(b))

print("Comparisons between a==b",a==b)

print("Comparisons between a is b",a is b)



p = b"Hallo"
t = str(p)
u = t.encode("UTF-8")













