"""
This program reads the csv file month_tourists.csv and prints the data 
"""
import csv 

with open("month_tourists.csv", 'r') as file:
    reader = csv.reader(file)
    next(reader)
    year_1978 = dict()
    for row in reader:
        year_1978[row[0]] = row[3]

    max_tourists = max(year_1978.values())


    for k,v in year_1978.items():
        if v == max_tourists:
            print(f"The busiest month of 1978 was {k} with {v} tourists visiting")

