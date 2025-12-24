# For printing table of any number in Normal list methods
# a = int(input("Enter a number for printing its Table:- "))
# table = []
# for i in range(1,11):
#     table.append(a*i)
# print(table)



# Now using the List Comprehension 
a = int(input("Enter a number for printing its Table:- "))
table = [a*i for i in range(1,11)]
print(table)



# Even shorter without any list named table, just printing a nameLess table 
# a = int(input("Enter a number for printing its Table:- "))
# print([a*i for i in range(1,11)])


