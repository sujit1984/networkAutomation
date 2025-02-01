"""
This program parses the file network_devices.txt and captures each row as a list inside another list
"""

#import csv

devices = list()
with open('network_devices.txt', "r") as file:
    for line in file.read().splitlines():
        devices.append(line.split(":"))

print(devices)
