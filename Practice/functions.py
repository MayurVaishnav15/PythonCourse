def full_name(first,last):
    return f"{first},{last}"

print(full_name("mayur", "vaishnav"))


#______________________________________________________________________________________________________________

from itertools import repeat
# Numbers we want to raise to a power
bases = [2, 4, 8, 16]

# We want to raise every number in 'bases' to the power of 3
# repeat(3) creates an infinite stream of 3s: (3, 3, 3, 3, ...)
results = list(map(pow, bases, repeat(3)))

print(results)


#______________________________________________________________________________________________________________


# Raw data with extra spaces
raw_data = ["  10 ", " 25", "30  ", "  45"]

# 1. Strip whitespace and 2. convert to integer in one line
cleaned_data = list(map(int, map(str.strip, raw_data)))

print(cleaned_data)


#______________________________________________________________________________________________________________

square = lambda x: x*x
list1 = [1, 2, 3, 4, 5]
print(list(map(square,list1)))

 #OR
print(list(map(lambda x: x*x, list1)))

 #OR
from itertools import repeat # already imported above
print(list(map(pow,list1,repeat(2))))


#______________________________________________________________________________________________________________

def sum_of_digits(n):
    if n==0:
        return 0
    return n%10 + sum_of_digits(n//10)
print("The sum of digits is",(sum_of_digits(12345)))