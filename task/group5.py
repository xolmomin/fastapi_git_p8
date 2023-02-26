import csv
import json
import yaml

l=[]
with open('regions.csv', 'r') as f:
    f.readline()
    for row in csv.reader(f):
        data = {}
        data['id']=row[0]
        data['name']=row[1]
        l.append(data)
with open(r'group5.yaml', 'w') as file:
    documents = yaml.dump(l, file)

result = {}
with open('regions.csv') as file:
    file.readline()
    data = csv.reader(file)
    for i in data:
        result[i[0]]=i[1]

with open('group5.json','w') as f:
    json.dump(result,f,indent=2)
