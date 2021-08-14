from datetime import datetime
from time import sleep
import pytz
from datetime import date
import sys
# datetime object containing current date and time
now = datetime.now()
print("\n")
print("use ctrl C to close")

print("\n")
print("\n")
print("\n")
print("\n")


today = date.today()
print("  Date:", today)


print("-------------------------")

while True:
  sleep(0.01)
  tz_NY = pytz.timezone('America/Los_Angeles')
  datetime_NY = datetime.now(tz_NY)
  print( "  Time:", datetime_NY.strftime("%H:%M:%S"), end = '\r')
  
  
















