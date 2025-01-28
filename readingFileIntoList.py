"""
Reading files into lists
"""

# 1. f.read().splitlines()

with open("config.txt") as file:
    content = file.read().splitlines()
    print(content)
print('#'*50)
#f.readlines()

with open("config.txt") as file:
    content = file.readlines()
    print(content)
print('#'*50)
# f.readline()
with open("config.txt") as file:
    content = file.readline()
    print(content)
print('#'*50)
# list(f)

with open("config.txt") as file:
    content = list(file)
    print(content)