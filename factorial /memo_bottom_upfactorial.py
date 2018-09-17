import timeit
def factorial(n):
    ''' 
        This is a array-based solution for calculating factorials using a bottom up approach. 

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
    memo = {}
    memo[0]=1
    memo[1]=1

    for i in range(2,n+1):
        memo[i] = i*memo[i-1]
    
    return memo[n]


print(factorial(100))
#Wrapper for function arguments before using timeit
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
wrapped = wrapper(factorial, 100)
print(timeit.timeit(wrapped,number=1000))