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

for year in range(2009, 2013):
        for inspection in classifications:
                print(year, inspection)
                var = "{"
                var2 = "}"

                # sending post request and saving response as response object
                r = requests.post(FDA_endpoint, headers=header, data=data.format(var, var, year, inspection, var2, var2))

                # extracting response text
                pretty_json = json.loads(r.text)
                # print(json.dumps(pretty_json, indent=2))

                inspection_df = pd.DataFrame.from_dict(pretty_json)

                result = inspection_df['totalrecordcount'][0]

                print(result)
