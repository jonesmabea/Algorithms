#Author: Jones Agwata

import timeit
def fibonacci(n): 
    ''' 
    This is a simple recursive solution to the fibonacci problem. 

    f(n) = f(n-1)+f(n-2)...+f(n-n)
        where f(0) = 0, f(1) = 1

    Caveat: Fails when n~? due to recursive limit or when n~? due to stack overflow 

    params:
    --------
    n : int 
        n values to calculate fibonacci numbers

    returns:
    --------

    int
        fibonacci value for n values
    ''' 
    assert(n>=0), "N should be >= 0"
    if n <= 1  :
        return n 
    else: 
        return fibonacci(n-1)+fibonacci(n-2)

#Wrapper to bind function arguments before using timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
wrapped = wrapper(fibonacci, 100)
print(timeit.timeit(wrapped,number=1000))
print(fibonacci(100))