import csv
import json

csv_file = open('regions_group4.csv', 'r')
json_file = open('group4.json', 'w')

fieldnames = ('id', 'name')
reader = csv.DictReader(csv_file, fieldnames)
for row in reader:
    json.dump(row, json_file)
    json_file.write('\n')