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

print(fibonacci(100))

