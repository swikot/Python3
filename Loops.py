import sys
import random
__author__ = 'snow'



#1 Count-controlled loops
# for (i=0; i <= n; i++)
# Python doesn't know this kind of loop.

#2 Condition-controlled loop
# A loop will be repeated until a given condition changes
# There are while loops and do while loops with this behaviour.

# 3Collection-controlled loop
# This is a special construct which allow looping through the elements of a "collection"
#  which can be an array, list or other ordered sequence.

# Python supplies two different kinds of loops:
# the while loop and the for loop,
# which correspond to the condition-controlled loop and collection-controlled loop.

# A Simple Example with a While Loop

n=100
sum=0
counter=1

while counter<=n:
    sum+=counter
    counter+=1

print("sum %d: %d"%(n,sum))


# Using a while Loop for Reading Standard Input

# Python has these three channels as well:
# standard input
# standard output
# standard error
# They are contained in the module sys. Their names are:
# sys.stdin
# sys.stdout
# sys.stderror


text=""
while 1:
    c=sys.stdin.read(1)
    text=text+c
    if c=="\n":
        break


print("String is = %s"%text)


# its alternative is input() :p


# The else Part
# Similar to the if statement, the while loop of Python has also an optional else par
# The general syntax of a while loop looks like this:
#
# while condition:
# 	statement_1
# 	...
# 	statement_n
# else:
# 	statement_1
# 	...
# 	statement_n



# Premature Termination of a while Loop

n=20
to_be_gussed=int(n*random.random())-1

guess=0
while guess!=to_be_gussed:
      guess = int(input("New number: "))
      if guess>0:
          if guess>to_be_gussed:
              print("number is very large")
          elif guess<to_be_gussed:
              print("number is too small")
      else:
          print("Sorry I think you are giving up")
          break
else:
    print("congratulation you made it")


print("I like it")










