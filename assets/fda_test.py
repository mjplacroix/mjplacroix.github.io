import requests
import pandas as pd
import json



string_1 = """ 
        {
        multline line comment {} 
        another one {}
"""

string_2 = string_1.format("2018", "2020")

print(string_2)

exit()

data = """
        {
        "start": 1, 
        "rows":10,
        "returntotalcount" : true,
        "sort" : "FiscalYear",
        "sortorder" : "ASC",
        "filters" : {},
        "columns" : [
                "Classification: {}",
                "FiscalYear"
        ]
        }
                """

classifications = ['Voluntary Action Indicated (VAI)', 'No Action Indicated (NAI)', 'Official Action Indicated (OAI)']

annual_inspections_df = pd.DataFrame()

for year in range(2009, 2014):
        for num in range(0, 3):
                current_year = f'"FiscalYear":"{year}"'
                print(current_year)                
                query = data.format(current_year, classifications[num])
                print(query)


exit()



def get_specific_data(year, classification):

        print(f'Year: {year}')
        print(f'Class: {classification}')

        # defining the api-endpoint
        FDA_endpoint = "https://api-datadashboard.fda.gov/v1/inspections_classifications"      

        # data to be sent to api
        header = {"Content-Type": "application/json",
                "Authorization-User": "michael.jp.lacroix@gmail.com",
                "Authorization-Key": "WIBEC7KSOAABYID"
                }  

        # specific data requested 
        data = """
        {
        "start" : 1, 
        "rows":10,
        "returntotalcount" : true,
        "sort" : "FiscalYear",
        "sortorder" : "ASC",
        "filters" : {"FiscalYear":["2018"]},
        "columns" : [
                "Classification",
                "FiscalYear"
        ]
        }
                """

        # sending post request and saving response as response object
        r = requests.post(FDA_endpoint, headers=header, data=data)

        # extracting response text
        pretty_json = json.loads(r.text)
        # print(json.dumps(pretty_json, indent=2))

        inspection_df = pd.DataFrame.from_dict(pretty_json)

        result = inspection_df['totalrecordcount'][0]
        
        return result

exit()

# since FDA API is limited to 5000 data points per request, this is a
# nested for loop iteratively requesting each piece of data needed to display
# overall totalls


 
classifications = ['Voluntary Action Indicated (VAI)', 'No Action Indicated (NAI)', 'Official Action Indicated (OAI)']

annual_inspections_df = pd.DataFrame()

for year in range(2009, 2014):
        for num in range(0, 3):                
                result = get_specific_data(year, classifications[num])




