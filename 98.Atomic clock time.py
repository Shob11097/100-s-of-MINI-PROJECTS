#Atomic clock time

from datetime import datetime
datetime.now()

import ntplib
from time import ctime
c = ntplib.NTPClient()
response = c.request("europe.pool.ntp.org", version=3)
ctime(response.tx_time)