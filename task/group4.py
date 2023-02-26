import csv
import json
import yaml

csv_file = open('regions_group4.csv', 'r')
json_file = open('group4.json', 'w')

fieldnames = ('id', 'name')
reader = csv.DictReader(csv_file, fieldnames)
for row in reader:
    json.dump(row, json_file)
    json_file.write('\n')


csv_file = open('regions_group4.csv', 'r')
yaml_file = open('group4.yaml', 'w')

fieldnames = ('id', 'name')
reader = csv.DictReader(csv_file, fieldnames)
for row in reader:
    yaml.dump(row, yaml_file, default_flow_style=False)