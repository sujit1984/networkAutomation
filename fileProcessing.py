"""
Read the file devices.txt as a text file and get each line
as a llist

"""
list_of_devices=list()
with open("devices.txt") as file:
    next(file)
    for line in file.read().splitlines():
        content = line.split(':')
        list_of_devices.append(content)

print(list_of_devices)