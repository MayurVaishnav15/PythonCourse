""" Python Fetch Tuples faster than Lists as they are immutable
    Used as dictionary keys (since they are hashable)
    safe from unintendent modifications
"""
a = (2, 3, 5, 6, 8, 9)
print(a)
print(a[3])
# a[2]= 22  This is a type Error : tuple object does not support item assignment

b = (2,)  # Tuple with one Element needs COMMA "," after the element  

# Tuple Unpacking
tu = (3,2,21)
a,b,c= tu # This automatically assigns ...
print(a,b,c)

# Common Tuple Methods 
t = (3,12, 51, 23,12)
print(t.count(12))
print(t.index(12))