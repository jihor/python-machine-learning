import pandas as pd, numpy as np, timeit as ti

print(pd.Series(np.arange(101, 116)))       # series of int32's
print(pd.Series((1, 2, 3)))                 # series of int64's
print(pd.Series((1, "a", None)))            # series of objects
print(pd.Series((1, 2, None)))              # series of float64's, None converted to NaN
print(pd.Series(["Test", "me", "gently"]))

s1 = pd.Series({1: "b", 2: -478, 3: None})
print(s1)         # zero column values are inferred from dict keys
print(s1.index)   # index = int64

s2 = pd.Series({1: "b", 2: -478, "x": None})
print(s2)         # same,
print(s2.index)   # but index = object

s3 = pd.Series({"a": 1, "b": 2, "c": None})
print(s3)         # same + None converted to NaN
print(s3.index)

s = pd.Series({"a": 1, "b": 2, "c": None, 3: 3, 4: 278})
print(s.index)

print(pd.Series(["lily", "scott", "mike"], index=[10, 20, 30]))   # can pass index explicitly
s4 = pd.Series({30: "scott", 5: "mike", 20: "lily", 7: "rael", 10: "roxy"}, index=[10, 20, 30])   # any values not in index wil be ignored
print(s4)
print(s4[30])            # scott - queried by index label
print(s4.loc[30])        # scott - queried by index label
print(s4.iloc[2])        # scott - queried by index position

simple_sum = """
sum = np.int64(0)
for item in s5:
    sum += item
"""
print(ti.timeit(stmt=simple_sum, number=100, setup="import pandas as pd, numpy as np; s5 = pd.Series(np.arange(1000))"))
# series' own implementation is vectorized, and therefore faster
print(ti.timeit(stmt="s5.sum()", number=100, setup="import pandas as pd, numpy as np; s5 = pd.Series(np.arange(1000))"))

simple_increment = """
for item, value in s5.iteritems():
    s5.iloc[item] = value + 10
"""

print(ti.timeit(stmt=simple_increment, number=10, setup="import pandas as pd, numpy as np; s5 = pd.Series(np.arange(1000))"))
# same here, with even more relative speed gain
print(ti.timeit(stmt="s5 += 10 ", number=10, setup="import pandas as pd, numpy as np; s5 = pd.Series(np.arange(1000))"))

# Pandas values can be changed
s6 = pd.Series(np.arange(3))
print(s6)
s6.set_value(0, 100)
s6.iloc[1] = 200
print(s6)   # Values are changed
# but the index is immutable
s7 = s6.append(pd.Series(np.arange(2, 5)))
print(s6)   # Still the same
print(s7)   # Still the same
print(s7.loc[2])        # now returns a row set, a new Series object