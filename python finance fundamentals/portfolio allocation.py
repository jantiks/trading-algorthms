import pandas as pd
import quandl
import matplotlib.pyplot as plt
K_DAY = (252**0.5)
money = 1000000
start = pd.to_datetime("2012-01-01")
end = pd.to_datetime("2017-01-01")
aapl = quandl.get("WIKI/AAPL.11",start_date = start,end_date = end)
csco = quandl.get("WIKI/CSCO.11",start_date = start,end_date = end)
ibm = quandl.get("WIKI/IBM.11",start_date = start,end_date = end)
amzn = quandl.get("WIKI/AMZN.11",start_date = start,end_date = end)
for stock_df in (aapl,csco,ibm,amzn):
    stock_df["Normed Return"] = stock_df["Adj. Close"]/stock_df["Adj. Close"].iloc[0]

# 30% in aapl
# 20% in csco
# 40% in ibm
# 10% in amzn

for stock_df,allo in zip((aapl,csco,ibm,amzn),[.3,.2,.4,.1]):
    stock_df['Allocation'] = stock_df["Normed Return"]*allo

for stock_df in (aapl,csco,ibm,amzn):
    stock_df["Position Values"] = stock_df["Allocation"]*money
all_pos_vals = (aapl["Position Values"],csco["Position Values"],
                ibm["Position Values"],amzn["Position Values"])
portfolio_val = pd.concat(all_pos_vals,axis=1)
portfolio_val.columns = ["aapl pos.","csco pos.","ibm pos.","amzn pos."]
portfolio_val["Total sum"] = portfolio_val.sum(axis=1)
portfolio_val["Daily return"] = (portfolio_val["Total sum"]/portfolio_val["Total sum"].shift(1))-1
SR = (portfolio_val["Daily return"].mean())/portfolio_val["Daily return"].std()
ASR = K_DAY * SR
print(ASR)