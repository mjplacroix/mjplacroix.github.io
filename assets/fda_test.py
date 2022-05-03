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

for year in range(2009, 2014):
        print(year)

        data = """
        {
        "start" : 1, 
        "rows":10,
        "returntotalcount" : true,
        "sort" : "FiscalYear",
        "sortorder" : "ASC",
        "filters" : {"FiscalYear":["{}"]},
        "columns" : [
                "Classification",
                "FiscalYear"
        ]
        }
                """

        data.format(year)
        # sending post request and saving response as response object
        r = requests.post(FDA_endpoint, headers=header, data=data)

        # extracting response text
        pretty_json = json.loads(r.text)
        # print(json.dumps(pretty_json, indent=2))

        inspection_df = pd.DataFrame.from_dict(pretty_json)

        print(inspection_df.shape)
        print(inspection_df.head())
