"""
Writing lines into a text file.
"""

with open("writefile.txt", 'w') as file:
    file.write("this is the first line\n")


# writing into the same file by appending

with open("writefile.txt", 'a') as file:
    file.write("This is the second line\n")

# Opening a file in read + write mode

with open("writefile.txt", 'r+') as file:
    file.seek(10)
    file.write("600")
    file.seek(0)
    print(file.read())
    print(file.tell())



