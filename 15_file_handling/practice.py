# with open("notes.txt","w") as f:
#     f.write("Learning python is fun...")

# with open("notes.txt","r") as f:
#     print(f.read())

# with open("tasks.txt","w") as f:
#     f.write("Line 1\n")
#     f.write("Line 2 \n")
#     f.write("Line 3\n")

# with open("tasks.txt","a") as f:
#     f.write("Task Completed")

# with open("tasks.txt","r") as f:
#     for lines in f.readlines():
#         print(lines)

# import os

# a= os.getcwd()   # tells about current working directory
# print(a)

# b = os.listdir() # list all the files in our current folder
# print(b)

# os.mkdir("myfolder") # makes new folder in the current folder


# import shutil

# shutil.copy("tasks.txt","myfolder")
# shutil.move("tasks.txt","myfolder")

# import sys
# def count_lines(filename):
#     with open(filename) as f:
#         return len(f.readlines())
# python .\15_file_handling\practice.py tasks.txt   run this  type of command in terminal to run this code
# if __name__ == "__main__":
#     filename = sys.argv[1]
#     num_lines = count_lines(filename)
#     print(f"The total lines in {filename} are {num_lines}")

# import sys  
# def search_word(word,string):
#     return string.count(word)

# if __name__ == "__main__":
#     filename = sys.argv[1]
#     word = sys.argv[2]
#     with open(filename) as f:
#         string = f.read()   #Opening the file and storing it in temp string variable 
#         n = search_word(word,string)
#         print(f'There are {n} occurances of word "{word}" in filename {filename}')



# Write a program that reads a file and creates another file with all words converted to uppercase.
with open("tasks.txt","r") as f:
    lower_case = f.read()
    upper_case = lower_case.upper()
    print(upper_case)

with open("new_File","w") as f:
    f.write(upper_case)