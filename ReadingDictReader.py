import csv
with open('DictReader.csv') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)
