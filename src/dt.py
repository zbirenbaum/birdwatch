from textwrap import indent
from time import sleep
import pandas as pd
from sheetrel import get_locdict
import wunderwrap
import json

wr = wunderwrap.WunderWrapper()
returndata = {}

locdict = get_locdict()
counter = 0
to_dict = {}
to_dict['locations'] = []
print(
        len(
            list(
                set(
                    locdict.keys()
                    )
                )
            )
        )
for key in locdict.keys():
    if counter < 0:
        geocode = locdict[key]['geocode']
        returned = wr.get_pws_near_geo(geocode)
        result = returned
        try:
            test=result['location']
        except:
            print(result)
        to_dict['locations'].append({
            'original' : key, 
            'geocode' : geocode,
            'actual' : locdict[key]['realname'],
            'result' : result
            })
#        counter = counter +1
    else:
        break
#js = json.dumps(to_dict, sort_keys=True, indent=4)
#jsonFile = open("../apisave/geosearchpws.json", "w")
#jsonFile.write(js)
#jsonFile.close()
#backtodict = json.loads(js)
#print(pd.read_json(js))
#print(dict)
