# For READ
f = open("text.txt","r")   # rt for reading text,,,,,, rb for reading binary
content = f.read()
print(content)
f.close()


# For WRITE
message = "hello , this is a file made to learn write in python"
f = open("write.txt","w")
content = f.write(message)
f.close()


# APPEND to an existing file 
message = """ 
This is a message to get append"""
f = open("write.txt","a")
content = f.write(message)
f.close