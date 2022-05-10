import requests
import pandas as pd
import json


# defining the api-endpoint
FDA_endpoint = "https://api-datadashboard.fda.gov/v1/inspections_classifications"      

# data to be sent to api
header = {"Content-Type": "application/json",
        "Authorization-User": "michael.jp.lacroix@gmail.com",
        "Authorization-Key": "WIBEC7KSOAABYID"
        }  

# specific data requested 
data = """
{}
"start" : 1, 
"rows":10,
"returntotalcount" : true,
"sort" : "FiscalYear",
"sortorder" : "ASC",
"filters" : {}
        "FiscalYear":["{}"],
        "Classification":["{}"]
        {},
"columns" : [
        "Classification",
        "FiscalYear"
]
{}
        """

classifications = ['Voluntary Action', 'No Action', 'Official Action']

records_df = pd.DataFrame(columns=['year', 'VAI', 'NAI', 'OAI'])

for year in range(2009, 2017):
        year_records = []
        year_records.append(year)
        print(year_records)
        for inspection in classifications:
                # print(year, inspection)
                var = "{"
                var2 = "}"

                # sending post request and saving response as response object
                r = requests.post(FDA_endpoint, headers=header, data=data.format(var, var, year, inspection, var2, var2))

                # extracting response text
                pretty_json = json.loads(r.text)
                # print(json.dumps(pretty_json, indent=2))

                inspection_df = pd.DataFrame.from_dict(pretty_json)

                result = inspection_df['totalrecordcount'][0]

                year_records.append(result)

                if len(year_records) == 4:
                        print(year_records)
                        records_df.loc[len(records_df)] = year_records
                        # records_df = pd.concat([records_df, year_records])
                        print(records_df)




print(records_df)

data = records_df.to_json('./inspections.json', orient='index')
print(data)
