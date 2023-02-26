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



filename = 'regions.csv'

def convert_row(headers, row):
    s = f'<row id="{row[0]}">\n'
    for header, item in zip(headers, row):
        s += f'<{header}>' + f'{item}' + f'</{header}>\n'
    return s + '</row>'


with open(filename, 'r') as f:
    r = csv.reader(f)
    headers = next(r)
    xml = '<data>\n'

    for row in r:
        xml += convert_row(headers, row) + '\n'

    xml += '</data>'

with open('group3.test', 'w') as f:
    f.write(xml)
