# r for reading
# w for writing file
file1 = open("sample.txt", "r")
print(file1.name)
fileStuff = file1.read()
print("file 1 stuff")
print(fileStuff)
file1.close()

# with statement will automatically closed the file
with open("sample.txt", "r") as file1:
    FileContent = file1.read()
    print(FileContent)
