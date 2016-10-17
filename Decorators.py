__author__ = 'swikot'

def succ(first,*l):
    print("sum of the list is: ",(first+sum(l)))

list=[1,2,3,4,6,7]

successor=succ

# now
successor(*list)
succ(*list)
# The next important fact is that we can delete either "succ" or "successor" without deleting the function itself
# del succ
# successor(*list)


