import csv
import json
import yaml


with open("group1.json") as file:
    s = json.load(file)

with open("group1.yaml", "w") as file:
    yaml.dump(s, file)


