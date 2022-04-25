import requests
pload = {'username':'Olivia','password':'123'}
r = requests.post('https://httpbin.org/post',data = pload)
print(r.text)

exit()

# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "https://api-datadashboard.fda.gov/v1/inspections_classifications"


# your source code here
source_code = '''
print("Hello, world!")
a = 1
b = 2
print(a + b)
'''

# data to be sent to api
data = {'Content-Type': "application/json",
        'Authorization-User': "michael.jp.lacrox@gmail.com",
        'Authorization-Key': "WIBEC7KSOAABYID"
        }

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)

# extracting response text
pastebin_url = r.text   
print("The pastebin URL is:%s"%pastebin_url)



"""
POST /inspections_classifications
Content-Type: application/json
Authorization-User: michael.jp.lacrox@gmail.com
Authorization-Key: WIBEC7KSOAABYID
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