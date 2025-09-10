# fib series is series having 0,1 at start then every number is sum of previous 2 consecutive numbers
def fib(n):
    if(n==0 or n==1):
        return n
    return fib(n-2) + fib(n-1)
print(fib(7))