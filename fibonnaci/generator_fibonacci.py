a,b = 0,1
def fibonacci():
    global a,b
    ''' 
    This solution uses a generator

    f(n) = f(n-1)+f(n-2)...+f(n-n)
        where f(0) = 0, f(1) = 1

    params:
    --------

    returns:
    --------

    generator 
    ''' 
    while True: 
        a,b = b,a+b
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
    genseq=iter(genseq)
    for i in range(n):
        res = next(genseq)

    return res

f = fibonacci()
print(extract(100,f))
    
    