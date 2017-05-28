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

import numpy as np
import pandas as pd

timestamp = pd.Timestamp("2017-12-31")
print(timestamp)   # Timestamp
dec17 = pd.Period("2017-12")
print(dec17)         # Month period
dec31_2017 = pd.Period("2017-12-31")
print(dec31_2017)      # Day period

times1 = pd.Series(["Dec 30th", "Dec 31st", "Jan 1st"], [pd.Timestamp("2017-12-30"), pd.Timestamp("2017-12-31"), pd.Timestamp("2018-01-01")])
print(type(times1.index))    # DatetimeIndex
print(times1.index > timestamp)
times2 = pd.Series(["Dec 2017", "Jan 2018", "Feb 2018"], [pd.Period("2017-12"), pd.Period("2018-01"), pd.Period("2018-02")])
print(type(times2.index))    # PeriodIndex
# can compare to timestamp
print(times2.index > timestamp)
# but can't compare to index with other frequency
# print(times2.index > dec31_2017)
print(times2.index > dec17)

dec30_2017 = pd.to_datetime("30.12.2017", dayfirst=True)
print(dec30_2017)

# when converted to timestamp, period takes its start as value
delta = dec31_2017.to_timestamp() - dec30_2017
print(delta)

df = pd.DataFrame({"SomeValue": np.random.randint(0, 100, 12)}, index=pd.date_range('2017-12-31', periods=12, freq='W-SAT'))
print(df)
df_mean = df.resample("M").mean()
print(df_mean)
print(df["2018-03":])

import matplotlib.pyplot as plt

plt.plot(df)
plt.grid(True)
plt.show()
