import csv
import pandas as pd



northloccols = [0,1,2,3,4]
southloccols = [5,6,7,8,9]
northlocarrival = [10,11,12,13,14]
southlocarrival = [15,16,17,18,19]




datelabels = ['2015', '2016', '2017', '2018', '2019']
labels = ['northloc', 'southloc', 'northarrive', 'southarrive']
birddict = {}
for date in datelabels:
    birddict[date] = {}
    for label in labels:
        birddict[date][label] = []


with open('sheetrelevant.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count < 2:
            line_count = line_count + 1
            continue
        else:
            for colnum in range(len(row)):
                year = str(int(colnum)%5 + 2015)
                print(colnum%4)
                datatype = list(birddict[year].keys())[int(colnum)%4]
                print(row[colnum] + datatype)
                birddict[year][datatype].append(row[colnum])
            

reform = {(outerKey, innerKey): values for outerKey, innerDict in birddict.items() for innerKey, values in innerDict.items()}
dfloader = pd.DataFrame(reform).T#df = df.explode('southloc')

dataframedict = {}
for dateindex in datelabels:
    dataframedict[dateindex] = dfloader.loc[dateindex].T


#for dframe in dataframedict:
  #  print(dataframedict[dframe])
    
