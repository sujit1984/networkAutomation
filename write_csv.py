"""
This program writes a new row in a csv file and also creates another new csv file and adds rows to it
"""

import csv

with open("names.csv","a") as csvfile:
    writer = csv.writer(csvfile)
    csvdata = (5,"Pranshu", "Mumbai")
    writer.writerow(csvdata)

with open("numbers.csv","w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['x', 'x**2', 'x**3'])
    for i in  range (1,11):
        writer.writerow([i, i**2, i**3, i**4])

