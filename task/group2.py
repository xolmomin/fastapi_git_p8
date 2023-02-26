import csv
import pandas as pd

f = open('regions.csv')
csv_f = csv.reader(f)
data = []

for row in csv_f:
    data.append(row)
f.close()

df = pd.read_csv('regions.csv')
header = list(df.columns)


def convert_row(row):
    str_row = """<%s>%s</%s> \n""" * (len(header) - 1)
    str_row = """<%s>%s""" + "\n" + str_row + """</%s>"""
    var_values = [list_of_elments[k] for k in range(1, len(header)) for list_of_elments in [header, row, header]]
    var_values = [header[0], row[0]] + var_values + [header[0]]
    var_values = tuple(var_values)
    return str_row % var_values


text = """<collection shelf="Regions">""" + "\n" + '\n'.join(
    [convert_row(row) for row in data[1:]]) + "\n" + "</collection >"
print(text)
with open('group2.xml', 'w') as myfile:
    myfile.write(text)
