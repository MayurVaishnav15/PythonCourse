def sum(a,b):
    c=a+b  # a and b are local variables  
    z=1    # this is a new varible z (local), have existence in only this function 
    return c

def greet():
    z= 32 # Local variable
    print("Hello world! ")
    return

z = 45 
print(sum(4,5))
print(greet())
print(z)