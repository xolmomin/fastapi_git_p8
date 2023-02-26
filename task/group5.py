import csv
import json
import yaml

data = []
with open('regions.csv', 'r') as f:
    f.readline()
    for row in csv.reader(f):
        data.append(row)
with open(r'group5.yaml', 'w') as file:
    documents = yaml.dump(data, file)

result = []
with open('districts.csv') as file:
    data = csv.reader(file)
    for i in data:
        result.append(i)

with open('districts.json', 'w') as f:
    json.dump(result, f, indent=2)
