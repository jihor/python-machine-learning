import pandas as pd, numpy as np, timeit as ti

# Series
print("Series")
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
print(s4[[10, 30]])      # roxy, scott - slicing
print(s4[0:40])          # roxy, lily, scott - slicing using range
print(s4.loc[30])        # scott - queried by index label    (loc is not method, it's an attribute with __getitem__ and __setitem__ methods defined)
print(s4.iloc[2])        # scott - queried by index position (same with iloc)

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
# same with removing rows
s7 = s6.append(pd.Series(np.arange(2, 5)))
s8 = s7.drop(2)
print(s8)        # now returns a row set, a new Series object
print(s7)   # Still the same
print(s8)
s7.drop(2, inplace=True)
print(s7)   # Changed

# DataFrame is a two-axis Series
print("\nDataFrames")
person1 = {"name": "Dmitry", "age": 29, "sex": "male"}
person2 = {"name": "Helga", "age": 30, "sex": "female"}
person3 = pd.Series({"name": "Mike", "age": 31, "sex": "male"})
person4 = pd.Series({"name": "Justine", "age": 26, "sex": "female"})
df1 = pd.DataFrame([person1, person2, person3, person4])
# indexes on both axis can be non-unique
df2 = pd.DataFrame([person1, person2, person3, person4], index=["p1", "p1", "p2", "p2"])
print(df2.loc["p1"])
print("\n", df2.loc["p1", "name"])
# chaining is relatively slow. It also returns copy of the data instead of the original.
print("\n", df2.loc["p1"]["age"])
# can't select column-wise directly, have to transpose the data frame. Use carefully.
print("\n", df2.T.loc["name"])
# slicing is also supported
print("\n", df2.T.loc[:])
print("\n", df2.loc[:, ("age", "sex")])
print("\n", df2[["age", "sex"]])         # same

# append() and drop() work as in Series, creating copies by default

# There is a difference in slicing:
# series[label(s)] -> scalar value / series for row set
# dataframe[colname(s)] -> series for the colname / dataframe with selected columns