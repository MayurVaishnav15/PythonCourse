import os

a = os.listdir("09_Loops")  # Print List of all files and folder inside the requested folder
print(a)
print(os.getcwd())          # tells us that in which working directory we are in currently

if os.path.exists("10_strings"):     # tells if given directory exists or not 
    print("Yes it exists.")
else:
    print("It do not exists")

# os.remove("sample.txt")  # os.remove only deletes the file , NOT folders
# os.rmdir("samplefile")   # Only used to remove empty Folders/Directory