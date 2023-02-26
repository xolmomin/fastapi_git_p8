import csv
import json
import yaml

with open('regions.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    json_data = list(reader)

with open('group1.json', 'w') as jsonfile:
    json.dump(json_data, jsonfile, indent=4)

with open("group1.json") as file:
    s = json.load(file)

with open("group1.yaml", "w") as file:
    yaml.dump(s, file)
