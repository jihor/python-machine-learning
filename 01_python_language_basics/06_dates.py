from supplemental_functions import add_numbers
import datetime
import datetime as dt # can also alias imported packages
import time as tm

print(add_numbers(1, 2, 3))

print(datetime.date.today())
print(dt.date.today())
t = tm.time()
print(t)        # Timestamp in epoch seconds
print(dt.date.fromtimestamp(t) == dt.date.today())
delta = dt.timedelta(days=180)
print(dt.date.today() - delta)
