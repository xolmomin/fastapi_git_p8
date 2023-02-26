print("Ravshanjon")
print("Nusratullo")
print("Dilshod")

import csv
import json
result = []
with open('districts.csv') as file:
    data = csv.reader(file)
    for i in data:
        result.append(i)

with open('districts.json','w') as f:
    json.dump(result,f,indent=2)
