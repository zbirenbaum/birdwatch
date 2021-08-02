import aiohttp
import asyncio
import json
import os 
from aiohttp import ClientSession
from formatreq import formatreq
import datetime
import getdates as gd
import time

def get_full_dates():
    start = datetime.datetime.strptime("01-01-2015", "%d-%m-%Y")
    end = datetime.datetime.strptime("01-01-2020", "%d-%m-%Y")
    dates = gd.get_time_range_list(start, end)
    return dates

async def retry(url, session):
    response = None
    try:
        response = await session.request(method='GET', url=url)
        response.raise_for_status()
        response_json = await response.json()
        #print(f"Response status ({url}): {response.status}")
        print('success')
        return response, response_json
    except Exception as err:
        return err

async def get_book_details_async(geocode, date, session):
    url = formatreq(geocode=geocode, date=date)
    try:
        response = await session.request(method='GET', url=url)
        response.raise_for_status()
        response_json = await response.json()
        #print(f"Response status ({url}): {response.status}")
        return response, response_json
    except Exception as err:
        print(err)
        #return await retry(url, session)


async def run_program(geocode, date, session):
    """Wrapper for running program in an asynchronous manner"""
    dateval = date[0] + '-' + date[1]
    try:
        responsecode, response = await get_book_details_async(geocode, date, session)
        if response is not None: 
            directory = 'responses/_' + geocode
            if not os.path.exists(directory):
                 os.makedirs(directory)
            with open(directory + '/'+ dateval + '.json', 'w+') as f:
                json.dump(response, f)
                f.close()
        else:
            directory = 'logs/_' + geocode
            if not os.path.exists(directory):
                 os.makedirs(directory)
            with open(directory + '/'+ dateval + '.json', 'w+') as f:
                f.write(str(responsecode.url))
                f.close()
        #return response
        #print(f"Response: {json.dumps(parsed_response, indent=2)}")
    except Exception as err:
#        with open('failed.txt', 'a+') as f:
#            f.write(str(err))
#            f.close()
#        directory = 'logs/_' + geocode
#        if not os.path.exists(directory):
#             os.makedirs(directory)
#        with open(directory + '/'+ dateval + '.json', 'w+') as f:
#            f.write(err.url)
#            f.close()
        #print(f"Exception occured: {err}")
        pass

async def begin(geocode=None, dates=None, tuplelist=None, urllist=None):
    async with aiohttp.ClientSession() as session:
        if urllist is not None:
            await asyncio.gather(*[run_program(geocode, date, session) for geocode, date in tuplelist])
        elif tuplelist is not None:
            await asyncio.gather(*[run_program(geocode, date, session) for geocode, date in tuplelist])
        else:
            await asyncio.gather(*[run_program(geocode, date, session) for date in dates])


def get_actualids(jsd):
    stationdict = {}
    for i in range(len(jsd['locations'])):
        location = jsd['locations'][i]
        try:
            actualid = location['actual'].replace(" ", "_")
            actualid = actualid.replace(",", "_")
            actualid = actualid.replace("/n", "")
            geo = location['geocode']
            stationdict[geo] = actualid
            continue
        except:
            #print('ERROR ' + location['actual'] + ' HAS NO DATA')
            continue
    return stationdict


def restore_data():
    file = open('../apisave/geosearchpws.json')
    jsd = json.load(file) 
    return jsd

apikey = 'e1f10a1e78da46f5b10a1e78da96f525'
jsd = restore_data()
actualdict = get_actualids(jsd)
#print(actualdict)
print(len(list(set(actualdict.keys()))))
locgeolist = list(actualdict.keys())
locgeodict = {}
actuals = []

retrylist=[]

dates = get_full_dates()
for dir in os.listdir('responses'):
    contents=os.listdir('responses/' + dir)
    contentlist=[]
    for content in contents:
        content = content.removesuffix('.json')
        contentlist.append(content.split('-'))
    if len(contentlist) > 30 and len(contentlist) < 60:
        for date in dates:
            if date not in contents:
                retrylist.append((str(dir)[1:],date))

print(len(retrylist))
#locgeolist=retrylist
#print(retrylist)
#print(len(retrylist))
tuplelist = []
geo = '53.546125,-113.493823'
for date in dates:
    tuplelist.append((geo,date))

#for geo, date in tuplelist:
#    print(date)
#for geo in locgeolist:
loop = asyncio.get_event_loop()
loop.run_until_complete(begin(tuplelist=retrylist))
#ret = begin(locgeolist[0], dates)
