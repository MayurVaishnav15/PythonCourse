# name = "mayur vaishnav" 
# print(name[0])
# print(name[-1])
# print(len(name))


text = "Python Programming"
print(text[0:6]) # first 6 characters
print(text[-6:]) # last 6 characters
print(text[::2]) # every second character starting from index 1


#reversing text using slicing
texts = "Hello World"
print(texts[::-1]) 

#stripping text
text = " Python Programming   "
print(text.strip())  # removes leading and trailing whitespace
print(text.title())  # converts to title case
print(text.count('o'))  # counts occurrences of 'o'


# checking if alphanumeric
text = "abc1234"
print(text.isalnum()) # True if all characters are alphanumeric