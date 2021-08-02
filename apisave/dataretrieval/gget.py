import grequests
import datetime
import os
from formatreq import formatreq
import getdates as gd
import time

class GGet:
    def __init__(self, locgeolist):
        dates = get_full_dates()
        reqlist = []
        for geocode in locgeolist:
            for date in dates:
                req = formatreq(geocode=geocode, date=date)
                reqlist.append(req)
        self.reqlist=reqlist

    def exception(self, request, exception):
        print("Problem: {}: {}".format(request.url, exception))

    def runner(self):
        results = grequests.map((grequests.get(u) for u in self.reqlist), exception_handler=self.exception, size=60)
        print(results)

def get_full_dates():
    start = datetime.datetime.strptime("01-01-2015", "%d-%m-%Y")
    end = datetime.datetime.strptime("01-01-2020", "%d-%m-%Y")
    dates = gd.get_time_range_list(start, end)
    return dates

retrylist=[]
for dir in os.listdir('responses'):
    if len(os.listdir('responses/' + dir)) == 0:
        retrylist.append(str(dir)[1:])
locgeolist=retrylist
greq = GGet(retrylist)

result = greq.runner()


