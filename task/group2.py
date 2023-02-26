import csv
import pandas
import yaml

""" Reading whole csv file with panda library """
df = pandas.read_csv('regions.csv')

""" Dump DataFrame into getData.yml as yaml code """
with open('group2.yaml', 'w') as outfile:
    yaml.dump(
        df.to_dict(orient='records'),
        outfile,
        sort_keys=False,
        width=72,
        indent=4
    )
