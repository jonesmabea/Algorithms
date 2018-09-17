#Author: Jones Agwata

import timeit
def fibonacci(n):
    ''' 
    This is a memoized solution using a bottom up approach to the fibonacci problem. 

    f(n) = f(n-1)+f(n-2)...+f(n-n)
        where f(0) = 0, f(1) = 1

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
    memo={}
    memo[0]=0
    memo[1]=1
    for i in range(2,n+1,1):
        memo[i] = memo[i-1]+memo[i-2]
             
    return memo[n]

#Wrapper for function arguments before using timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
wrapped = wrapper(fibonacci, 20)
print(timeit.timeit(wrapped,number=1000))
# print(fibonacci(100))

