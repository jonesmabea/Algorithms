from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    ''' 
    This solution uses the naive recursion silution and the inbuilt python lru cache to solve the recursion problem in the 
    naive implementation.

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
    if n <= 1  :
        return n 
    else: 
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(100))