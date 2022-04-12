#   a Python program to read a given CSV file as a dictionary
# let's say we have an existing bookreeads csv file
import csv

with open('bookreeads.csv', 'r') as csvfile:
    dta= csv.DictReader(csvfile)
    for row in dta:
        print(row['Book(s)'], row['Author'])
print(row)