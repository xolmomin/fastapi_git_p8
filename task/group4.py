import csv
import json

csv_file = open('regions.csv', 'r')
json_file = open('data.json', 'w')

fieldnames = ('id', 'name')
reader = csv.DictReader(csv_file, fieldnames)
for row in reader:
    json.dump(row, json_file)
    json_file.write('\n')