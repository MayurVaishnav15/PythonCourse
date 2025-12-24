marks = [5,2,21,6,33]
print(marks)
marks.append(63)
print(marks)
marks.pop()
print(marks)
marks.insert(1,'33','11')
print(marks)


marks = [13, 55, 64,99,]
mixed = ["34", "hello", "3","2", "False","?","/"]
extra_marks = [33,55,66,65]

print(marks[2:4])
print(marks[2])
print(mixed[3:6]) 
# print(mixed.insert(2,[2,3,4]))    This line return none because List.insert() do not return any value.
# mixed.insert(2,[2,3,4])
print(mixed)  
marks.extend(extra_marks)    # Adds extra_marks list to marks list
print(marks)
marks.sort()
print(marks)
mixed.sort()
print(mixed)