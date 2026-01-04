s={1,2,3,4,5,6,7,8,9,10}
print(s)
# print(s[2])  This is not possible in sets because sets store unordered elements with no index

#Set Methods
s.add(11)
print(s)

s.remove(1)    # will give error if element is not present in set.
print(s)

s.discard(21)  # will not give error if element is not present in set.
print(s)

s.pop()        # randomly pops any element and return its value.
print(s)


s1={1,2,3,4,5}
s2={3,4,5,33}
#UNION
c = s1.union(s2)
print(c)
#Intersection
c = s1.intersection(s2)
print(c)
#Difference   = elements in s1 which are not present in element 2
c = s1.difference(s2)
print(c)