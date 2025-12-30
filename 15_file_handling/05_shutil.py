import shutil

# shutil.rmtree("directory_name")  # It deletes the whole directory and the content inside it 

shutil.copy("write.txt","john.txt") # Content of write.txt will be copied to john.txt

shutil.move("file_name", "directory_name/")  # moves content of that file into diretory 