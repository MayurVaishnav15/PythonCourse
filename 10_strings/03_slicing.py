name = "mayur123456789"
print(name[0:3])
print(name[0:-1]) #this will be taken as 0 to (5-1) that is 4 ,,so [0:4]
                  # and as they print till n-1 , 0 to 3 will be printed


 #skip characters slicing:-
print(name[0:8:2]) #this last two means skip one character 


# if some numbers are not available
print(name[:4]) #it takes first empty as zero always i.e. [0:4]
print(name[0:]) #it takes the second empty as length full i.e. [1:14]