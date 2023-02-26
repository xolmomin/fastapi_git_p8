print('Nasrulloh')
print('Xolmomin')
print('Diyorbek')
print('Ozoda')

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