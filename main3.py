import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['email'])

