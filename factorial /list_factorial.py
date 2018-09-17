import timeit 
from functools import reduce
import operator


def factorial(n):
    ''' 
        This is a array-based solution for calculating factorials. 

        n! = n * (n-1)! 
            where 0! = 1, 1! = 1


        params:
        --------
        n : int 
            value to calculate factorial

        returns:
        --------

        int
            factorial value for n
        ''' 
    assert(n>=0), "N should be >= 0"
    nums= [x for x in range(1,n+1)]
    return reduce(operator.mul, nums, 1)

# print(factorial(100))
#Wrapper for function arguments before using timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
wrapped = wrapper(factorial, 100)
print(timeit.timeit(wrapped,number=1000))
