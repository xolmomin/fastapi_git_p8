import csv, yaml

data = []

with open('regions.csv') as reg:
    csvReader = csv.DictReader(reg)
    for rows in csvReader:
        data.append(rows)

with open('group3.yaml', 'a') as yamlF:
    yaml.dump(data, yamlF)
#
# data = csv.reader(csv_file, delimiter=',', quotechar='"')
# d = []
# for index, row in enumerate(data):
#     if index == 0:
#         d = row
#     else:
#         new_yaml = open('group3.yaml', 'w')
#         yaml_t = ""
#         for index, raw in enumerate(row):
#             ls = "   "
#             raw_head = d[index].lower().replace(" ", "_").replace("-", "")
#             if (raw_head == "source"):
#                 lineSeperator = '  - '
#
#             cell_text = ls + raw_head + " : " + raw.replace(" ", ", ") + " "
#
#             yaml_t += cell_text
#         print(yaml.dump(yaml_t))


