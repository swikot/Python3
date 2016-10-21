__author__ = 'snow'
# simple iterator
cities = ["Paris", "Berlin", "Hamburg", "Frankfurt", "London", "Vienna", "Amsterdam", "Den Haag"]
for locations in cities:
    print("locations: ",locations)


print("\n")
capitals = { "France":"Paris",
             "Netherlands":"Amsterdam",
             "Germany":"Berlin",
             "Switzerland":"Bern",
             "Austria":"Vienna"}

for loc in capitals:
    print(loc,":",capitals[loc])


print()
print()
# generators
def city_generator():
    yield("London")
    yield("Hamburg")
    yield("Konstanz")
    yield("Amsterdam")
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")


city=city_generator()
print(next(city))
print(next(city))
print(next(city))
print(next(city))
print(next(city))
print(next(city))
print(next(city))
print(next(city))


# Method of Operation

def fibonacci(n):
    """Ein Fibonacci-Zahlen-Generator"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)
for x in f:

    print(x, " ", end="") #
print()







import itertools














