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

# sending post request and saving response as response object
r = requests.post(API_ENDPOINT, data = data, json=)

# extracting response text
print(r.text) 


json = """
        {
            "start" : 1,
            "rows" : 10,
            "sort" : "ProductCode",
            "sortorder" : "ASC",
            "filters" : {
                "FEINumber":[3003378587,1000117386,3008091479]
            },
            "columns" : [
                "FEINumber",
                "FirmName",
                "CountryCode",
                "ProductCode",
                "RefusalDate"
            ]
        }
        """