import csv
import yaml
from xml.etree import ElementTree as ET

csv_file = open('regions_group4.csv', 'r')
csv_file.readline()

fieldnames = ('id', 'name')
reader = csv.DictReader(csv_file, fieldnames)

root = ET.Element('data')
for row in reader:
    item = ET.SubElement(root, 'item')
    id_elem = ET.SubElement(item, 'id')
    id_elem.text = row['id']
    name_elem = ET.SubElement(item, 'name')
    name_elem.text = row['name']

xml_data = ET.tostring(root)

with open('group4.xml', mode='wb') as xml_file:
    xml_file.write(xml_data)

    csv_file = open('regions_group4.csv', 'r')
    csv_file.readline()
    fieldnames = ('id', 'name')
    reader = csv.DictReader(csv_file, fieldnames)
    data = {'data': []}
    for row in reader:
        data['data'].append({'id': row['id'], 'name': row['name']})

    yaml_data = yaml.dump(data)
    with open('group4.yaml', mode='w') as yaml_file:
        yaml_file.write(yaml_data)
