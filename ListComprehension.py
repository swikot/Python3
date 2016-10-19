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
