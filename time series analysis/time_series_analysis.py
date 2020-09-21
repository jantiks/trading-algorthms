import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#------statsmodels indroduction------#
# df = sm.datasets.macrodata.load_pandas().data
# df.index = sm.tsa.datetools.dates_from_range("1959Q1","2009Q3")
# gdp_cycle,gdp_trend = sm.tsa.filters.hpfilter(df["realgdp"])
# df["trend"] = gdp_trend
# df[["realgdp","trend"]].loc["2000-03-31":].plot()
# plt.show()

# #-------EWMA-------#
# airline = pd.read_csv("airline_passengers.csv",index_col="Month")
# airline.dropna(inplace=True)
# airline.index = pd.to_datetime(airline.index)
# # airline["sma6"] = airline["Thousands of Passengers"].rolling(6).mean()
# # airline["sma12"] = airline["Thousands of Passengers"].rolling(12).mean()
# # airline[["Thousands of Passengers","sma6","sma12"]].plot()
# airline["ewm12"] = airline["Thousands of Passengers"].ewm(span=3).mean()
# airline[["Thousands of Passengers","ewm12"]].plot()
# plt.show()


#---------ETS---------#
from statsmodels.tsa.seasonal import seasonal_decompose
airline = pd.read_csv("airline_passengers.csv",index_col="Month")
airline.dropna(inplace=True)
airline.index = pd.to_datetime(airline.index)
result = seasonal_decompose(airline["Thousands of Passengers"],model="multiplicative")
result.plot()
plt.show()