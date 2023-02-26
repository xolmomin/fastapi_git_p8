import csv
import json
import yaml
import xml.etree.ElementTree as gfg

data = []
with open("regions.csv", 'r') as file:
    csvreader = csv.reader(file)

    for i in csvreader:
        d = {"id": i[0],
             "name": i[1]}
        data.append(d)

root = gfg.Element("regions")

for i in data:
    b1 = gfg.SubElement(root, "id")
    b1.text = i.get('id')
    b2 = gfg.SubElement(root, "name")
    b2.text = i.get("name")

tree = gfg.ElementTree(root)
with open("group5.xml", 'wb') as file:
    tree.write(file)

l = []
with open('regions.csv', 'r') as f:
    f.readline()
    for row in csv.reader(f):
        data = {}
        data['id'] = row[0]
        data['name'] = row[1]
        l.append(data)
with open(r'group5.yaml', 'w') as file:
    documents = yaml.dump(l, file)

result = []
with open('regions.csv') as file:
    file.readline()
    data = csv.reader(file)
    for i in data:
        d = {}
        d['id'] = i[0]
        d['name'] = i[1]
        result.append(d)
with open('group5.json', 'w') as f:
    json.dump(result, f, indent=2)
