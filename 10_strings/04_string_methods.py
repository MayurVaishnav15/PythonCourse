#Strings are immutable , they cant be changed
# name[0] = "k"  This is error as strings can't be changed 
name = " \n maYur vaishnav "
a =len(name)
print(a)

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title()) 


print(name.strip())  # this remove starting and ending both blank lines 
print(name.lstrip()) # this will remove starting blank line
print(name.rstrip()) # this won't remove the starting blank line



text = "Python is fun and fun and fun "
print(text.find("is"))                # tells index no. of starting i
print(text.replace("fun","awesome"))  # all fun are replaced 

text = "apple,banana,mango"
print(text.split(","))
print(",".join(['apple', 'banana', 'mango']))

line = "Python, is dynamically typed language"
print(line.split(","))


texts = " p ython1234"
print(texts.isalpha())  #print True if all char in string is alphabets
print(texts.isdigit())  #print true if all char are number in string
print(texts.isalnum())  #print true if all char are mixture of alph & number
print(texts.isspace())  #print true if string contain a  space