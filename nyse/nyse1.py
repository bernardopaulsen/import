import pandas as pd
import pickle
import yahoo

with open("nyse.pickle","rb") as file:
    tickers = pickle.load(file)

print(len(tickers))

i  = 0
l  = len(tickers)
df = pd.DataFrame()
print(i)
for ticker in tickers:
    i += 1
    try:
        stock      = yahoo.get(ticker,(1991,1,1),(2021,1,1))
        df[ticker] = stock["Ret"]
        print(i/l, f"{ticker} OK")
    except:
        print(i/l, f"{ticker} --")

with open("nyse_prices.pickle","wb") as file:
    pickle.dump(df,file)
