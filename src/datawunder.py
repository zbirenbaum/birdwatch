import pandas as pd
import wunderwrap

wr = wunderwrap.WunderWrapper()

loc='NZAA:9:NZ'

years=['2011', '2011'] #max 31days
months=['06','07']
days=['15','15']
start=years[0]+months[0]+days[0]
end=years[1]+months[1]+days[1]

respjson=wr.stationdaily(loc,start,end).json()
obslist=wr.getobservations(respjson)
#wr.printjsonkeys(respjson)
df=pd.json_normalize(obslist).dropna(axis=1)

dates = ['expire_time_gmt', 'valid_time_gmt']
df[dates]=(df[dates]).apply(pd.to_datetime, unit='s')
print(df)
#dfobs = dfobs.append(dfItem, ignore_index=True)    

#df[dates]=df[dates].apply(lambda t: wr.timeconv(t))
# def buildframe(obslist): 
#     dfobs = pd.DataFrame()  
#     for item in obslist:
#         dfItem = jsonToDataFrame(obslist)                
#         dfobs = dfobs.append(dfItem, ignore_index=True)    
#    return dfobs

