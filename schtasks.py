import os, random
from datetime import datetime, timedelta

"""
Cmd console to run: schtasks /create /tn SecurityScan /sc once /st HH:MM /sd MM:DD:YYYY /tr *task repository address

Linux/based systems have the cron equivalent
"""

if os.system("schtasks /query /tn SecurityScan") == 0:
  os.system("schtasks /delete /f SecurityScan")

print("I am doing malicious things")

filedir = os.path.join(os.getcwd(), "schtasks.py")

maxInterval = 1
interval = 1+(random.random()*(maxInterval-1))
dt = datetime.now() + timedelta(minutes=interval)
t = "%s:%s" % (str(dt.hour).zfill(2), str(dt.minute).zfill(2))
d = "%s/%s/%s" % (str(dt.month), str(dt.day).zfill(2), dt.year)

os.system('schtasks /create /tn SecurityScan /tr "'+filedir+'" /sc once /st '+t+' /sd '+d)

input()