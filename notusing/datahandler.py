import pandas as pd

impdf = pd.read_csv('sheetrelevant.csv',index_col=[1], mangle_dupe_cols=False)
print(impdf)
