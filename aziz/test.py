import json
import pandas as pd

js = '20190101-20190131.json'
dictobj = json.load(open(js,'r'))

print(dictobj.keys())

obs = dictobj['observations']
print(len(obs))
print(obs[0]['pressure_desc'])

df = pd.DataFrame.from_dict(obs)
print(df)

df.to_csv('temp.csv')
