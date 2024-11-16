import csv
import json
import pandas as pd

with open('data/in/Arztsuche.json', encoding='utf-8') as inputfile:
    data = json.loads(inputfile.read())
    df = pd.json_normalize(data)

df.to_csv('data/out/Doctors_api.csv', encoding='utf-8', index=False, quoting=csv.QUOTE_ALL, sep=';')
