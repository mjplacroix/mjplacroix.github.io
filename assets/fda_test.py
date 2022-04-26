import requests
pload = {'username':'Olivia','password':'123'}
r = requests.post('https://httpbin.org/post',data = pload)
print(r.text)

# defining the api-endpoint
API_ENDPOINT = "https://api-datadashboard.fda.gov/v1/inspections_classifications"

# data to be sent to api
data = {'Content-Type': "application/json",
        'Authorization-User': "michael.jp.lacrox@gmail.com",
        'Authorization-Key': "WIBEC7KSOAABYID"
        }

json = """
{
    "start": 1,
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
r = requests.post(API_ENDPOINT, data = data, json=json)

# extracting response text
print(r.text) 
