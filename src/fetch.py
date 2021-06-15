import pandas as pd
import requests
url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/" #+{endpoint} base url
dfbase = pd.read_csv("aydata.csv")
token = "YbeEiJeZxRfsrjrFWpYMqhHVlKMSAdjc"
header = { "token" : token }
#stationtest = requests.get(url+"stations", headers=header).json()
#locationtest = requests.get(url+"locations", headers=header).json()['results']
#locationtest = requests.get(url+"data?datasetid=GHCND&stationid=GHCND:COOP010008", headers=header).json()
#locationtest = requests.get('http://www.ncdc.noaa.gov/cdo-web/api/v2/datasets?datasetid=GSOM&stationid=COOP010008', headers=header) 
#print(stationtest)&stationid=GHCND:ZI000067964&limit=31
#locationtest = requests.get('http://www.ncdc.noaa.gov/cdo-web/api/v2/locations?datacategoryid=TEMP', headers=header).json()
locationtest = requests.get('http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCN-Daily', headers=header)
#results = locationtest['results']
print(locationtest)
#curl -H "token:<token>" "url"
#$.ajax({ url:<url>, data:{<data>},  })
#curl -H "token:<token>" "url" The token obtained from the token request page.
#$.ajax({ url:<url>, data:{<data>}, headers:{ token:<token> } })
