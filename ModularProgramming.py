import fibonacci
import builtins
import math



print("Fibonacci series is : ")
for i in range(11):
    fib=fibonacci.fib(i)
    print(fib,end=" ")

print()
for i in dir(math):
    print(i)

print(math.factorial(5))

