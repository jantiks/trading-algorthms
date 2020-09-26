import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import quandl
# start = pd.to_datetime("2012-01-01")
# end = pd.to_datetime("2017-01-01")
# aapl = quandl.get("WIKI/AAPL.11",start_date = start,end_date = end)
# csco = quandl.get("WIKI/CSCO.11",start_date = start,end_date = end)
# ibm = quandl.get("WIKI/IBM.11",start_date = start,end_date = end)
# amzn = quandl.get("WIKI/AMZN.11",start_date = start,end_date = end)
# stocks = pd.concat([aapl,csco,ibm,amzn],axis=1)
# stocks.columns = ["apple","cisco","ibm","amazon"]
# ret = stocks.pct_change(1)#daily return
# log_ret = np.log(stocks/stocks.shift(1))#logarithmic daily return
# log_ret.hist(bins=100)
# plt.show()
np.random.seed(101)
start = pd.to_datetime("2012-01-01")
end = pd.to_datetime("2017-01-01")
aapl = quandl.get("WIKI/AAPL.11",start_date = start,end_date=end)
csco = quandl.get("WIKI/CSCO.11",start_date = start,end_date=end)
ibm = quandl.get("WIKI/IBM.11",start_date = start,end_date=end)
amzn = quandl.get("WIKI/AMZN.11",start_date = start,end_date=end)
sotcks = pd.concat([aapl,csco,ibm,amzn],axis=1)
sotcks.columns = ["apple","cisco","ibm","amazon"]
log_ret = np.log(sotcks/sotcks.shift(1))# logarithmic return (we will use it for daily returns)
# print(log_ret.cov())#calculates the relationship between collumns
num_ports = 5000
all_weights = np.zeros((num_ports,len(sotcks.columns)))
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)
for ind in range(num_ports):
    #weights
    weights = np.array(np.random.random(4))#random allocation weights
    weights = weights/weights.sum()#rebalancing weights
    #save weights
    all_weights[ind,:] = weights
    #expected return
    ret_arr[ind] = np.sum((log_ret.mean()*weights)*252)
    #expected volatility
    vol_arr[ind] = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov() * 252, weights)))

    sharpe_arr[ind] = ret_arr[ind]/vol_arr[ind]
max_sr_vol = vol_arr[sharpe_arr.argmax()]
max_sr_ret = ret_arr[sharpe_arr.argmax()]
plt.scatter(vol_arr,ret_arr,c = sharpe_arr,cmap="plasma")
plt.scatter(max_sr_vol,max_sr_ret,c="red",s=50,edgecolors="black")
plt.colorbar(label = "sharp ratio")
plt.xlabel("Volatility")
plt.ylabel("return")
plt.show()