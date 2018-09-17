import timeit 
import itertools

a,b = 1,1 
def factorial():

    ''' 
        This is a simple recursive solution for calculating factorials 
        using the inbuilt lru cache to store frequent results. 

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
    global a,b
    while True:
        a = a*b
        b+=1 
        yield a
    

def extract(n,genseq):
    ''' 
    Extracts the nth value from a generator. 


    params:
    --------
    n : int  


    genseq : generator sequence


    returns:
    --------

    int 
    ''' 

    for i in range(n):
        res = next(genseq)
    return res
f = factorial()
# print(extract(100,f))
#Wrapper for function arguments before using timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
wrapped = wrapper(extract, 100,f)
print(timeit.timeit(wrapped,number=1000))
    