import csv
import json
# import yaml

data = []
with open('regions.csv', 'r') as f:
    f.readline()
    for row in csv.reader(f):
        data.append(row)
# with open(r'group5.yaml', 'w') as file:
#     documents = yaml.dump(data, file)

result = []
with open('regions.csv') as file:
    file.readline()
    data = csv.reader(file)
    for i in data:
        d={}
        d['id']=i[0]
        d['name']=i[1]
        result.append(d)
with open('group5.json','w') as f:
    json.dump(result,f,indent=2)
