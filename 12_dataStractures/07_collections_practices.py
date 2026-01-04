# #Q1
# fruits = ["apple","banana","orange"]
# print(fruits[0])
# print(len   (fruits))
# fruits[1]= "cherry"
# print(fruits)
# print(len(fruits))

# list1= [i for i in range(1,11)]
# print(list1)
# print(list1[0:3]) # first Three numbers
# print(list1[-3:len(list1)]) # last Three number  ,,,,,, another way print(list1[-3:])


# #Q2
# numbers = [5,2,9,1,7]
# numbers.sort()
# print(numbers)

# numbers.append(10)
# print(numbers)

# numbers.remove(2)
# print(numbers )

# numbers.insert(1,44)
# print(numbers)


# #Q3
# coordinates = (10,20)
# print(coordinates[1])
# print(coordinates[0])
# #coordinates[0] = 33 # Cannot happen as tuples are immutable
# list = list(coordinates)
# list[0]= 33
# coordinates=tuple(list)
# print(coordinates)

# #Q4
# my_set = {1,2,3,4,5}  # removes duplicate by default 
# my_set.add(5)
# my_set.remove(2)
# print(my_set)
# if 4 in  my_set:
#     print("Yes")
# else:
#     print("NO")

# #Q4
# dict = {"name":"alice","age":"55","grade":"A+"}
# print(dict)
# print(dict["grade"])
# dict["grade"]="A++"
# print(dict)
# dict["city"]="delhi"
# print(dict)
# print(dict.items()) #messy output 
# for keys,values in dict.items():
#     print(keys,values)




# def remove_duplicates(numbers):

   
#     '''
#     Remove duplicates from a list using a set.

#     Parameters:
#         numbers (list): A list of integers or floats.

#     Returns:
#         list: A new list with duplicates removed.
#     '''
#     return list(set(numbers))

 
# nums = [1, 2, 3, 2, 4, 1, 5, 3]
# print("Original list:", nums)
# print("Without duplicates:", remove_duplicates(nums))


# def most_expensive_product(products):
#     return max(products.items() )



# products = {
#     "Phone": 60000,
#     "Laptop": 80000,
#     "Tablet": 35000,
#     "Monitor": 15000
# }

# product, price = most_expensive_product(products)
# print(f"The most expensive product is '{product}' with price {price}.")


# #merging dictionary
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}

# d1.update(d2)
# print(d1)