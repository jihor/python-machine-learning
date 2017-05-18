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

# Reading files
print("\nReading files")
df = pd.read_csv("./data/09_pandas/features_with_values.csv", index_col=0)
print(df)

df2 = pd.read_csv("./data/09_pandas/target_values.csv")
df2["Height in meters"] = pd.read_csv("./data/09_pandas/features.csv")
df2.set_index("Height in meters", inplace=True)
print(df2)   # same as df

print(df2[1.80:])   # index range

df3 = df2.where(df2["Total number of sexual partners by age 30"] % 2 == 0)  # using a boolean mask
print(df3)
print(df3.dropna())   # drop NaN's

df4 = df2[df2["Total number of sexual partners by age 30"] % 2 == 0]
print(df4)            # shortcut to apply boolean mask and drop NaN's

# boolean masks support bit-wise AND and OR operations
df5 = df2[(df2["Total number of sexual partners by age 30"] % 2 == 0) & (df2["Total number of sexual partners by age 30"] > 3)]
print(df5)
df6 = df2[(df2["Total number of sexual partners by age 30"] % 2 == 0) | (df2["Total number of sexual partners by age 30"] > 10)]
print(df6)

df["Sex"] = pd.read_csv("./data/09_pandas/more_features.csv").values          # add new column
df = df.assign(SexAgain=pd.read_csv("./data/09_pandas/more_features.csv").values)  # same
print(df)
# Column projection. Index column will be included automatically
# print(df[["Height in meters", "Total number of sexual partners by age 30", "Sex"]])
df = df[["Total number of sexual partners by age 30", "Sex"]]
print(df)
df.reset_index(inplace=True)   # can't reindex with moving primary key to secondary in one op, have to reset index
print(df)
df.set_index(["Sex", "Height in meters"], inplace=True)  # now we have a compound key
print(df)
print(df.loc[[("F", 1.80), ("M", 1.96)]])
df.index.names = ["s", "h"]    # rename
df = df.append(pd.Series(data={'Total number of sexual partners by age 30': 10}, name=('M', '1.88')))

# Apparently there is no way to insert a Series by compound index
# df.loc[('M', '1.89')] = pd.Series({"Total number of sexual partners by age 30": 10})
# But insert by one column is possible:
df.loc[('M', '1.89'), "Total number of sexual partners by age 30"] = 10
print(df)

df.loc[('M', '1.91'), "Total number of sexual partners by age 30"] = None
print(df)
df.fillna(0)
print(df)

time_df = pd.read_csv("./data/09_pandas/time_series.csv", index_col=0)
time_df.sort_index()
time_df = time_df.ffill(axis=0)  # ffill is an alias for fillna(method='ffill')
print(time_df)
