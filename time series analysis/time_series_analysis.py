import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import datetime

#------statsmodels indroduction------#
df = sm.datasets.macrodata.load_pandas().data
df.index = sm.tsa.datetools.dates_from_range("1959Q1","2009Q3")
gdp_cycle,gdp_trend = sm.tsa.filters.hpfilter(df["realgdp"])
df["trend"] = gdp_trend
df[["realgdp","trend"]].loc["2000-03-31":].plot()
plt.show()