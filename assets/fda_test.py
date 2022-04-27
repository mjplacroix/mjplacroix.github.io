import requests

# defining the api-endpoint
FDA_endpoint = "https://api-datadashboard.fda.gov/v1/inspections_classifications"

# data to be sent to api
data = {'Content-Type': "application/json",
        'Authorization-User': "michael.jp.lacrox@gmail.com",
        'Authorization-Key': "WIBEC7KSOAABYID"
        }       

json = """
{
    "start": 4,
    "rows": 10,
    "sort": "LegalName",
    "sortorder": "ASC",
    "returntotalcount": true,
    "filters": {
        "InspectionEndDateFrom": [
            "2001-11-27"
        ],
        "InspectionEndDateTo": [
            "2020-11-27"
        ]
    },
    "columns": [
        "FEINumber",
        "LegalName",
        "CitationID",
        "InspectionID",
        "InspectionEndDate"
    ]
}
        """

# sending post request and saving response as response object
r = requests.post(FDA_endpoint, data=data, json=json)

# extracting response text
print(r.text) 
