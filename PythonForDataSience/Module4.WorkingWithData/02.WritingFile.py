# r for reading
# w for writing file
file1 = open("sample.txt", "w")
file1.write("tung")

with open('sample.txt', 'w') as writefile:
    writefile.write("This is line A")