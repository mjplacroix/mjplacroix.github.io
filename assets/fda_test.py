import requests
import pandas as pd
import json

# defining the api-endpoint
FDA_endpoint = "https://api-datadashboard.fda.gov/v1/inspections_classifications"      

# data to be sent to api
data = {'Content-Type': "application/json",
        'Authorization-User': "michael.jp.lacroix@gmail.com",
        'Authorization-Key': "WIBEC7KSOAABYID"
        }       

json = """
{  "start" : 1,
    "rows" : 10,
    "sort" : "InspectionEndDate",
    "sortorder" : "ASC",
    "filters" : {
        "InspectionEndDateFrom":["2001-11-27"],
        "InspectionEndDateTo":["2020-11-27"]
    },
    "columns" : [
        "FEINumber",
        "LegalName",
        "InspectionID",
        "Classification",
        "InspectionEndDate"
    ]
}
        """
# sending post request and saving response as response object
r = requests.post(FDA_endpoint, headers=data, json=json)

# extracting response text
# print(r.text)

# data = r.json()
# print(data)

json_data = json.loads(r.text)

print(json_data)
