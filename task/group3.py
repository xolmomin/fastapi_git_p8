import csv
filename = 'regions.csv'
def convert_row(headers, row):
    s = f'<row id="{row[0]}">\n'
    for header, item in zip(headers, row):
        s += f'<{header}>' + f'{item}'
    return s + '</row>'
with open(filename, 'r') as f:
    r = csv.reader(f)
    headers = next(r)
    xml = '<data>\n'
    for row in r:
        xml += convert_row(headers, row) + '\n'
    xml += '</data>'


with open('grouop3.xml', 'w') as f:
    f.write(xml)