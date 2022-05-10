import requests
import pandas as pd
import json


data_df = pd.read_csv('inspections.csv')

data = data_df.to_json(orient='records')

parsed = json.loads(data)
for row in parsed:
    # pop the first dict key off each row
    # could be a good place for a list comprehension
    print(row.pop(['Unnamed']))
    print(json.dumps(row, indent=2))

# print(json.dumps(parsed, indent=2))