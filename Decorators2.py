
# def greet(name):
#     return "hello "+name
#
# greet_someone = greet
# print (greet_someone("John"))

def greet1(name):
    def get_message():
        return "Hi "

    result=get_message()+name
    return result

print(greet1("swikot"))

# Functions can be passed as parameters to other functions
def greet2(name):
   return "Hello " + name

def call_func(func):
    other_name = "John"
    return func(other_name)

print (call_func(greet2))
# function can return other function
def call_composure():
    def call_composure_inner():
        return "hello john this is inner function"
    return call_composure_inner()

call=call_composure
print("john is called here: ",call())
print()
# Inner functions have access to the enclosing scope
# more commonly known as closure


def call_composure_one(name):
    def call_composure_two():
        return "Hello "+ name +"!"

    return call_composure_two()

call_two=call_composure_one
print("call two is called from here : ",call_two("swikot"))

print()

# Composition of Decorators


def get_text(name):
    return "I am "+name

def p_decorate(func):
    def p_wrapper(name):
        print("before calling......")
        return func(name)
    return p_wrapper


my_calling=p_decorate(get_text)
print("my decorated value is: ",my_calling("swikot"))
get_text=p_decorate(get_text)
print(get_text("john"))

print()
# decorate with syntax

def p_decorate2(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

@p_decorate2
def get_text2(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print (get_text2("swikot"))




















