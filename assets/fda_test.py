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

data = """
{
    "start" : 1,
    "rows":100,
    "returntotalcount" : true,
    "sort" : "FiscalYear",
    "sortorder" : "ASC",
    "filters" : {
            "Classification":["Voluntary Action"],
            "InspectionEndDateFrom":["2018-11-27"]
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
r = requests.post(FDA_endpoint, headers=header, data=data)

# extracting response text
pretty_json = json.loads(r.text)
print(json.dumps(pretty_json, indent=2))
