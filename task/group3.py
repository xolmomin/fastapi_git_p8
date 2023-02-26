import csv, json, yaml

data = {}

with open('regions.csv') as reg:
    csvReader = csv.DictReader(reg)
    for rows in csvReader:
        print(rows)
        key = rows['\ufeffid']
        data[key] = rows

with open('group3.json', 'w') as jsonF:
    jsonF.write(json.dumps(data, indent=4))


data_y = []
with open('regions.csv') as reg:
    csvReader = csv.DictReader(reg)
    for rows in csvReader:
        data_y.append(rows)

with open('group3.yaml', 'w') as yamlF:
    yaml.dump(data_y, yamlF)

