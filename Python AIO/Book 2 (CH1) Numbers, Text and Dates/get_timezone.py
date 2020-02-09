# import datetime, give it an alias
import datetime as dt
# import timezone helpers from dateutil
from dateutil.tz import gettz

# UTC time right now
utc = dt.datetime.now(gettz('Etc/UTC'))
print(f"{utc:%A %D %I:%M %p %Z}")

sgt = dt.datetime.now(gettz('Asia/Singapore'))
print(f"{sgt:%A %D %I:%M %p %Z}")
