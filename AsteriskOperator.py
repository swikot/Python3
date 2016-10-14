__author__ = 'swikot'


list1=[1,2,3,5,6,7]

a,*c,d=list1

print(a)
print(*c)
print(d)


x,*y,z=range(11)
print(x)
print(y,"   ",*y)
print(z)


# sometimes we need to split up an array
sep=[0,1,2,3,4,5,6,7,8,9]

#Old way
# p,q=sep[0],sep[1:]
# print(p)
# print(q)

# new approach
first,*rest=sep

print("first element is :",first)
print("Last element is :",rest)





my_list=[1,2,3,4,5,6,7,8,9]

def function(first,*rest):
    return (first+ sum(rest))

print("sum is finally:  ",function(*my_list))


my_list = [('a', 232),
           ('b', 343),
           ('c', 543),
           ('d', 23)]


print(list(zip(*my_list)))

my_list1=['a','b','c','d']
my_list2=[1,2,3,4]
my_list=list(zip(my_list1,my_list2))
print("now my List can be written as= : ",my_list)



def sum(a,b):  #receive args from function calls as sum(1,2) or sum(a=1,b=2)
    print(a+b)

my_tuple = (1,2)
my_list = [1,2]
my_dict = {'a':1,'b':2}

# Let us unpack data structure of list or tuple or dict into arguments with help of '*' operator
sum(*my_tuple)   # becomes same as sum(1,2) after unpacking my_tuple with '*'
sum(*my_list)    # becomes same as sum(1,2) after unpacking my_list with  '*'
sum(**my_dict)   # becomes same as sum(a=1,b=2) after unpacking by '**'

# output is 3 in all three calls to sum function.
# http://stackoverflow.com/questions/36901/what-does-double-star-and-star-do-for-python-parameters


























