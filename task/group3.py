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
