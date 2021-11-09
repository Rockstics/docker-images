#!/usr/bin/python3
import time

import pymongo
import datetime
import json
import coding
import chardet
# 获取前一天时间

start_day = datetime.datetime.today() - datetime.timedelta(days=31)
yesterday = datetime.datetime.today() - datetime.timedelta(days=1)

begin_time = start_day.strftime("%Y-%m-%d 00:00:00")
end_time = yesterday.strftime("%Y-%m-%d 23:59:59")

myclient = pymongo.MongoClient('mongodb://test:test@121.36.3.28:23000/test')

mydb = myclient["test"]
#collist = mydb.list_collection_names()
collist = ["total_bei7home"]


query = {"systime": {"$gte": begin_time, "$lte": end_time}}
print(query)


for col in collist:
    with open("mongo_export_%s.json" % col, "w+") as f:
        for row in mydb[col].find(query):
            row["_id"] = {"$oid": str(row["_id"])}
            row["currentDay"] = {"$date": '{0}Z'.format(
                datetime.datetime.isoformat(row["currentDay"], timespec='milliseconds'))}
            jdata = json.dumps(row)
            f.write(jdata + "\n")

#datetime.datetime.today()

