from os import replace
import pandas as pd

def get_locdict():
    fulldata = pd.DataFrame(pd.read_csv('sheetrel.csv'))
    locframe = pd.DataFrame(pd.read_csv('locations.csv'))
    locframe['Geocode'] = locframe.Longitude.astype(str) + ',' + locframe.Latitude.astype(str) #type: ignore
    listfullcols = list(fulldata.columns)

    #print(locframe)
    dict_locations = {}

    counter = 0
    reset = 0
    listproptuple = []
    listproptuple.append([])
    for i in range(9):
        if reset == 5:
            listproptuple.append([])
            counter = counter + 1
        fullcol = listfullcols[i]
        listproptuple[counter].append((fullcol, listfullcols[listfullcols.index(fullcol)+10]))
        reset = reset + 1

    #for locyear, arryear in listproptuple[0]: 
    #    hemidict = {'northern' : {
    #        locyear : None,

    #    }}
    #for i in range(4):
    #    for j in range(5):
    #        tuplevar = ()
    #    counter = counter + 1
        

    locframe['Geocode'] = locframe['Geocode'].str.replace(' ','')
    for label, series in locframe.iterrows():
        original = series['Original']
        actual = series['Actual']
        latitude = series['Latitude']
        longitude = series['Longitude']
        geocode = series['Geocode']
        dict_locations[original] = {
                'realname' : actual,
                'latitude' : latitude,
                'longitude' : longitude,
                'geocode' : geocode
                }
    return dict_locations

"""
for og in dict_locations.keys():
    linedict = line.to_dict() #type: ignore
    isin = fulldata.isin([og]).any()
    isin = isin[isin==True].index
    for col in isin:
        for tp in listproptuple:
            if tp[0] == col:
            return col, tp[1]


    line = fulldata[fulldata.eq(og).any(1)] #type: ignore
    dict_locations[og]['framedata'] = linedict



print(dict_locations)

collist = list(fulldata.columns)
#for col in collist: #type: ignore
originals = locframe['Original']

list_original = originals.to_list()

for original in list_original:
    row = locframe.loc['Original'] == original
     
    dict_locations[original] = {

            }


"""

#print(df.loc[collist] == name)

#print(df)
