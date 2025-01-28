"""
This program is used to read the contents of the passwd.csv file which contains a different delimiter than ,
"""

import csv

with open("passwd.csv",'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=":",lineterminator="\n")
    for row in reader:
        print(row)

print(csv.list_dialects())
