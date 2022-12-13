import codecs
import os
import time
import datetime
i=0
"""
time.sleep(5)
for i in range(0,1000):
    print("Task Scheduler running at -- " + str(datetime.datetime.now()))
    i=i+1
"""

file = codecs.open(r"C:\Users\hxkris\Desktop\favSitesTemplate.htm", "r", "utf-8")
print(file.read())

