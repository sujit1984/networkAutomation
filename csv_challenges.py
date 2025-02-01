"""
Challenge #1
Consider the following Python list:
people = [
['Dan', 34, 'Bucharest'],
['Andrei',21, 'London'],
['Maria', 45, 'Paris']
]
Using the CSV module write each element of the list (which is another list) into a CSV file called people1.csv
After writing into the file, read and print out the file contents.
Use the default , (comma) as the delimiter.
"""

import csv

# people = [
# ['Dan', 34, 'Bucharest'],
# ['Andrei',21, 'London'],
# ['Maria', 45, 'Paris']
# ]
#
# with open("people1.csv", 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     for item in people:
#         writer.writerow(item)
#
# with open("people1.csv",'r') as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         print(row)

"""
Challenge #2
Change the solution from the previous challenge and use : (colon) as the delimiter.

"""

people = [
['Dan', 34, 'Bucharest'],
['Andrei',21, 'London'],
['Maria', 45, 'Paris']
]

with open("people2.csv", 'w') as csv_file:
    writer = csv.writer(csv_file,delimiter=':')
    for item in people:
        writer.writerow(item)

with open("people2.csv",'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=":")
    for row in reader:
        print(row)