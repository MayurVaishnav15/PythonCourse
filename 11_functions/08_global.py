def sum (a,b):
    c = a+b
    global z # telling py  to modify global z
    z = 40
    return c
z = 34
print(sum(4,5))
print(z)