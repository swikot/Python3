__author__ = 'Swikot'

# general syntax of function
# def function-name(Parameter list):
#     statements, i.e. the function body

# simple function
def function_name():
    print("swikot")

function_name()

# calculating farhenhite


def farenhite(T_degrre_celcious):
    '''reture the temperature in degree farhenhite'''
    return T_degrre_celcious

print()
for i in (22.3,23.4,25.6):
    print(i," : ",farenhite(i))


# Optional Parameter

def hello_Name(name="everybody"):
    print("hello ",name)

hello_Name("swikot")
hello_Name()


# Docstring


def hello_func(name="everybody"):
    "hi all"

    print("hello",name)



print(hello_func.__doc__)



# Keyword Parameters

def sumsub(a, b, c=0, d=0):
    return a - b + c - d


print(sumsub(10,12))
print(sumsub(10,12,d=15))


# if u dont use it so the fuction looks like print(sumsub(42,15,0,10))

# Return Values

print("\n")
def no_return(x,y):
    c=x+y
    return c

res=no_return(4,5)
print("result is: ",res)



# Returning Multiple Values







































