student = {"name": "Alice", "age": 21, "grade": "A"}
print(student)

keys =(student.keys)
print(keys())
print(student.values())

print(student["name"])

print(student.pop("age"))  # POPs age and return the value in output
print(student)


# Dictionary Comprehension
table_of_5 = {i: 5*i for i in range(1,11)}
print(table_of_5)

squares = {i: i**2 for i in range(1,5)}
print(squares)

"""
5. When to Use Each Data Structure?

Data Structure       	Features	             Best For
List	                Ordered, Mutable	    Storing sequences, dynamic data
Tuple	                Ordered, Immutable	    Fixed collections, dictionary keys
Set	Unordered, Unique   Removing duplicates,    set operations
Dictionary          	Key-Value Pairs	        Fast lookups, structured data

"""