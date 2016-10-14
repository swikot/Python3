__author__ = 'snow'


# Formatted Output

p=1.2
q=1.3

print(str(p),":p",str(q),":p",str(p*q))

print("Art: %5d  price per unit %8.2f" %(453,59.058))
print("Art: {0:5d} price per unit {1:8.2f}".format(453,59.058))

print("First argument: {0}, second one: {1}".format(47,11))

print("various precions: {0:6.2f} or {0:6.3f}".format(1.4148) )

print("various precions: {a:6.2f} or {b:5d}".format(a=1.4148,b=6) )


# left justified and right justified

print("{0:<20s} {1:6.2f}".format('Spam & Eggs:', 6.99))

print("{0:>20s} {1:6.2f}".format('Spam & Eggs:', 6.99))



# If the width field is preceded by a zero ('0') character, sign-aware zero-padding for numeric types will be enabled.
# >>> x = 378
# >>> print("The value is {:06d}".format(x))
# The value is 000378
# >>> x = -378
# >>> print("The value is {:06d}".format(x))
# The value is -00378

# 	This option signals the use of a comma for a thousands separator.
# >>> print("The value is {:,}".format(x))
# The value is 78,962,324,245
# >>> print("The value is {0:6,d}".format(x))
# The value is 5,897,653,423
# >>> x = 5897653423.89676
# >>> print("The value is {0:12,.3f}".format(x))
# The value is 5,897,653,423.897





# Using dictionaries in "format"


print("The capital of {0:s} is {1:s}".format("Bangladesh","Dhaka"))
print("The capital of {country:s} is {capital:s}".format(country="Bangladesh",capital="Dhaka"))


data = dict(country="Ontario",capital="Toronto")
print("The capital of {country} is {capital}".format(**data))

capital_country = {"United States" : "Washington",
                   "US" : "Washington",
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

for c in capital_country:
    print("{country}: {capital}".format(country=c, capital=capital_country[c]))


print()
for c in capital_country:
    format_string = c + ": {" + c + "}"
    print(format_string.format(**capital_country))

# Using Local Variable Names in "format"




# Other string methods for Formatting

s = "Python"

print(s.center(10))


# ljust
# >>> s = "Training"
# >>> s.ljust(12)
# 'Training    '
# >>> s.ljust(12,":")
# 'Training::::'
# >>>



# rjust
# >>> s = "Programming"
# >>> s.rjust(15)
# '    Programming'
# >>> s.rjust(15, "~")
# '~~~~Programming'
# >>>


# zfill
# >>> account_number = "43447879"
# >>> account_number.zfill(12)
# '000043447879'
# >>> # can be emulated with rjust:
# ...
# >>> account_number.rjust(12,"0")
# '000043447879'
# >>>










































