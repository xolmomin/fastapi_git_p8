
import csv
data = []
with open("regions.csv", 'r') as file:

  csvreader = csv.reader(file)

  for i in csvreader:
    d = {"id" : i[0],
         "name" : i[1]}
    data.append(d)

import xml.etree.ElementTree as gfg

root = gfg.Element("regions")


for i in data:

  b1 = gfg.SubElement(root, "id")
  b1.text = i.get('id')
  b2 = gfg.SubElement(root, "name")
  b2.text = i.get("name")

tree = gfg.ElementTree(root)
with open("group5.xml" , 'wb') as file:
  tree.write(file)
