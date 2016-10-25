__author__ = 'snow'


# tuple=("A robot may not injure a human","A robot must obey human's order","A robot must defend a human")
#
#
# for count,items in enumerate(tuple):
#     print(count,":",items)


# instance counting calculator

class C:
    counter=0
    def __init__(self):
        type(self).counter+=1

    def __del__(self):
        type(self).counter-=1

if __name__=="__main__":
    a=C()
    b=C()
    print("created instance: ",C.counter)

    del a
    del b
    print("after destructor: ",C.counter)



