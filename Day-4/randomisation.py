# PYTHON RANDOM MODLUE
# Python Random module is an in-built module of Python which is used to generate random numbers.
# The random module provides some special methods for generating random integers.

import random
import lists
# You can see, lists is a another file and we have imported lists.py as a module over here and below is the procedure to return lists.py function.
print(lists.list)

random_integer = random.randint(1, 10)
print(random_integer)
# It will print any random number between 1 and 10 including 1 ands 10 too. Every time it'll generate new number.

random_float = random.random()
print(random_float)
# it will print float between 0 and 1 but, excluding 1.
# if we want to generate floating point number between 0-5 then, we will simply multiply the result of [random_float] with 5
print(random_float*5) # it will generate random floating point number between 0-5 but excluding 5
