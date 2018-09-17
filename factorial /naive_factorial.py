import timeit
def factorial(n):

    ''' 
        This is a simple recursive solution for calculating factorials. 

        n! = n * (n-1)! 
            where 0! = 1, 1! = 1

        Caveat: Fails when n~? due to recursive limit or when n~? due to stack overflow 

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
    if n==1 or n==1:
        return n 

    else: 
        return n * factorial(n-1)

# print(factorial(100))
#Wrapper for function arguments before using timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
wrapped = wrapper(factorial, 100)
print(timeit.timeit(wrapped,number=1000))