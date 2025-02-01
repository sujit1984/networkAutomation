import csv

csv.register_dialect('hashes', delimiter="#", quoting=csv.QUOTE_NONE,lineterminator='\n')
with open('items.csv','r') as csv_file:
    reader = csv.reader(csv_file,dialect='hashes')
    for row in reader:
        print(row)

## writing to a file with a dialect

with open('items.csv', 'a') as csv_file:
    writer = csv.writer(csv_file,dialect="hashes")
    item =['eraser', '8', '1.5']
    writer.writerow(item)

with open('items.csv','r') as csv_file:
    reader = csv.reader(csv_file,dialect='hashes')
    for row in reader:
        print(row)