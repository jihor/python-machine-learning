import numpy as np
import pandas as pd
import regex as re


def peta_to_giga(row):
    row["Energy Supply"] *= 1_000_000
    return row


def cleanup_names_energy(row):
    row["Country"] = re.split("\d", row["Country"])[0].split("(")[0].strip()
    return row

energy = (pd.read_excel("./data/01_data_processing/Energy Indicators.xls",
                        skiprows=17,
                        skip_footer=38,
                        names=["Country", "Energy Supply", "Energy Supply per Capita", "% Renewable"],
                        parse_cols="C:F")
          .replace("...", np.NaN)
          .apply(lambda row: peta_to_giga(row), axis=1)
          .apply(lambda row: cleanup_names_energy(row), axis=1)
          .reset_index()
          .set_index("Country")
          .rename(index={"Republic of Korea": "South Korea",
                         "United States of America": "United States",
                         "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                         "China, Hong Kong Special Administrative Region": "Hong Kong"})
          )

GDP = (pd.read_csv("./data/01_data_processing/API_NY.GDP.MKTP.CD_DS2_en_csv_v2.csv", skiprows=4)
       .reset_index()
       .set_index("Country Name")
       .rename(index={"Korea, Rep.": "South Korea",
                       "Iran, Islamic Rep.": "Iran",
                       "Hong Kong SAR, China": "Hong Kong"})
       .filter(items=np.arange(2006, 2016).astype("str"))  # well this filter looks stupid, there should be a simpler way :)
       )

ScimEn = (pd.read_excel("./data/01_data_processing/scimagojr.xlsx")
          .reset_index()
          .set_index("Country"))

# ScimEn is the smallest table, so it should be leading
df = (pd.merge(pd.merge(ScimEn[ScimEn["Rank"] <= 15], GDP, how="inner", left_index=True, right_index=True),
                   energy, how="inner", left_index=True, right_index=True)
      .filter(["Rank", "Documents", "Citable documents", "Citations", "Self-citations", "Citations per document", "H index", "Energy Supply", "Energy Supply per Capita", "% Renewable", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]))

print(df.filter(items=np.arange(2006, 2016).astype("str")).agg("mean", axis=1).sort_values(ascending=False))
