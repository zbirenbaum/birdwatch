import pandas as pd
import wunderwrap

wr = wunderwrap.WunderWrapper()
respjson=wr.stationdaily('NZAA:9:NZ','20110615','20110715').json()
obslist=wr.getobservations(respjson)
#wr.printjsonkeys(respjson)
df=pd.json_normalize(obslist).dropna(axis=1)
print(df)
#dfobs = dfobs.append(dfItem, ignore_index=True)    


# def buildframe(obslist): 
#     dfobs = pd.DataFrame()  
#     for item in obslist:
#         dfItem = jsonToDataFrame(obslist)                
#         dfobs = dfobs.append(dfItem, ignore_index=True)    
#    return dfobs

