import nntplib
from time import ctime
c = nntplib.NTPClient()
response = c.request('pool.ntp.org')
print ctime(response.tx_time)