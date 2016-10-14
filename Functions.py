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

















