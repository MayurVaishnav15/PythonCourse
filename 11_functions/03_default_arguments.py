def add(a,b,X=0):
    d = a + b+ X
    return d


sum = add(2,3,4) #if we do not pass three values here, then X will take the deful value we have set already as zero
print(sum)