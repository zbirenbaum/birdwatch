import wunderwrap as wr

wrapper = wr.WunderWrapper()

ret = wrapper.stationdaily('76585', '20151001')
print(ret.json())
