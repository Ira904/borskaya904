import csv
 
with open('Reader.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        print(row)