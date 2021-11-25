from datetime import datetime, timedelta
import time

dt1 = datetime(2021, 10, 25)
dt2 = datetime.now()
dt = datetime.strptime("2018/11/20", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(f"{dt.year}/{dt.month}")
dt = dt.strftime("%Y/%m")

print(dt)
print(dt2 > dt1)

duration = dt2 - dt1
print(duration)
print("days", duration.days)
print('seconds', duration.seconds)
print('total seconds', duration.total_seconds())

dt = datetime(2018, 11, 25) + timedelta(days=30, seconds=1000)
print(dt)
