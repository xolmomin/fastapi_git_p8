import csv
import json


with open('regions.csv', newline='') as csvfile:

    reader = csv.DictReader(csvfile)

    json_data = list(reader)


with open('group1.json', 'w') as jsonfile:
    json.dump(json_data, jsonfile, indent=4)



print('Zayniddin')
print('nuriddin')
print('javohir')




