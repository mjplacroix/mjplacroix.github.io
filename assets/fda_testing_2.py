import requests
import pandas as pd
import json


data_df = pd.read_csv('inspections.csv')

data = data_df.to_json(orient='records')
print(type(data))
parsed = json.loads(data)
print(type(parsed))

for row in parsed:
    print(row['year'])

    # pop the first dict key off each row
    # could be a good place for a list comprehension
    row.pop('Unnamed: 0')
    print(row)
    print(json.dumps(row, indent=2))

print(json.dumps(parsed, indent=2))

print(type(parsed))

with open('out_inspection_full.json', 'w') as f:
    json.dump(parsed, f)

exit()
data_df = pd.DataFrame(parsed)
data_df.to_json('./out_inspection_full.json', orient='index')