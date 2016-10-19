__author__ = 'snow'

# List comprehension is an elegant
# way to define and create
# list in Python
Celsius = [39.2, 36.5, 37.3, 37.8]

Far=[((float(9)/5)*x + 32) for x in Celsius]
print("far values",Far)

odd_number=[x for x in range(1,11) if x%2]
print("odd number is: ",odd_number)
even_number=[x for x in range(1,11) if x%2==0]
print("even number is: ",even_number)
list_tuples=[(x,y) for x in odd_number for y in even_number]
print("list tuples: ",list_tuples)

# Generator Comprehension
# use () instead of []
suare_x=(x**2 for x in range(21))
print("Generator List Comprehension: ",list(suare_x))
#  sieve of Eratosthenes

noprime=[j for i in range(2,8) for j in range(i*2,100,i)]
prime=[i for i in range(2,100) if i not in noprime]
print("prime numbers are: ",prime)

from math import sqrt
n=100

non_prime=[j for i in range(2,int(sqrt(n))) for j in range(i*2,100,i)]
primes=[i for i in range(2,100) if i not in non_prime]
print("prime numbers are: ",primes)


# Set Comprehension

n1=1000
key=int(sqrt(n1))
not_prime={j for i in range(2,key) for j in range(i*2,1000,i)}
primes={i for i in range(2,n1) if i not in not_prime}
print("set comprehension primes: ",primes)


# Recursive Function to Calculate the Primes

def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = {j for i in p for j in range(i*2, n+1, i)}
        p = {x for x in range(2, n + 1) if x not in no_p}
    return p

for i in range(1,50):
    print(i, primes(i))


# n Python 2, the loop control variable is not local,
# t can change another variable of that name outside of the list comprehension,
# x = "This value will be changed in the list comprehension"
# res = [x for x in range(3)]
# res
# [0, 1, 2]
#  x
# 2
# res = [i for i in range(5)]
# i
# 4
#


#in python 3
# $ python3
# Python 3.2 (r32:88445, Mar 25 2011, 19:28:28)
# [GCC 4.5.2] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> x = "Python 3 fixed the dirty little secret"
# >>> res = [x for x in range(3)]
# >>> print(res)
# [0, 1, 2]
# >>> x
# 'Python 3 fixed the dirty little secret'
# >>>