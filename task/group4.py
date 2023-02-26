import csv
import yaml

csv_file = open('regions_group4.csv', 'r')
yaml_file = open('group4.yaml', 'w')

fieldnames = ('name', 'age', 'gender')
reader = csv.DictReader(csv_file, fieldnames)
for row in reader:
    yaml.dump(row, yaml_file, default_flow_style=False)
import csv
from xml.etree import ElementTree as ET

csv_file = open('regions_group4.csv', 'r')
xml_file = open('group4.xml', 'w')

fieldnames = ('id', 'name')
reader = csv.DictReader(csv_file, fieldnames)

root = ET.Element('data')
for row in reader:
    item = ET.SubElement(root, 'item')
    for key, value in row.items():
        child = ET.SubElement(item, key)
        child.text = value

xml_file.write(ET.tostring(root).decode())






import csv
import yaml

csv_file = open('regions_group4.csv', 'r')
yaml_file = open('group4.yaml', 'w')

fieldnames = ('id', 'name')
reader = csv.DictReader(csv_file, fieldnames)
for row in reader:
    yaml.dump(row, yaml_file, default_flow_style=False)