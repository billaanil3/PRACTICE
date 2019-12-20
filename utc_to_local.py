import datetime
import pytz    # $ pip install pytz
import tzlocal
# $ pip install tzlocal

local_timezone = tzlocal.get_localzone()
# print local_timezone
# now = datetime.datetime.now()
# xxx = now.strftime("%Y-%m-%d %H:%M:%S")
utc_time = datetime.datetime.utcnow()
# utc_time = datetime.datetime.strptime(xxx, "%Y-%m-%d %H:%M:%S")
print utc_time
local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
print local_time
