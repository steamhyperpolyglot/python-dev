import datetime as dt
from dateutil.tz import gettz

event = dt.datetime(2020, 7, 4, 19, 0, 0)
print("Local: " + f"{event:%D %I:%M %p %Z}\n")

event_singapore = event.astimezone(gettz("Asia/Singapore"))
print(f"{event_singapore:%D %I:%M %p %Z}")
