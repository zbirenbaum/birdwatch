import os
import getdates as gd
import datetime
import time
def get_full_dates():
    start = datetime.datetime.strptime("01-01-2015", "%d-%m-%Y")
    end = datetime.datetime.strptime("01-01-2020", "%d-%m-%Y")
    dates = gd.get_time_range_list(start, end)
    return dates
def getmin(min):
    dates = get_full_dates()
    retrylist=[]
    counter = 0
    contents = None
    for dir in os.listdir('responses'):
        counter = counter + 1
        contents = os.listdir('responses/' + dir)
        if len(contents) < min:
            #min = len(contents)
            mincontents = contents
            minloc = dir
            retrylist.append(str(dir)[1:])
    return mincontents,minloc, retrylist

contents,dir, numretries = getmin(60)

print(contents)
print(len(contents))
print(len(numretries))
#print(len(numretries))
#while(1):
#    newretries = len(getnum(60))
#    if(newretries < numretries):
#        print(newretries)
#        numretries=newretries
#    time.sleep(0.5)
