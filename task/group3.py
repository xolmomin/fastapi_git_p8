import csv, yaml

data_y = []
with open('regions.csv') as reg:
    csvReader = csv.DictReader(reg)
    for rows in csvReader:
        data_y.append(rows)

with open('group3.yaml', 'w') as yamlF:
    yaml.dump(data_y, yamlF)
