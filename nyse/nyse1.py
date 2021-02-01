import pandas as pd
import pickle
import progress
import yahoo

with open("nyse.pickle","rb") as file:
    tickers = pickle.load(file)

print(len(tickers))

i  = 0
l  = len(tickers)
df = pd.DataFrame()
progress.update(0)
for ticker in tickers:
    i += 1
    try:
        stock      = yahoo.get(ticker,(1991,1,1),(2021,1,1))
        df[ticker] = stock["Ret"]
        progress.update(i/l, f"{ticker} OK")
    except:
        progress.update(i/l, f"{ticker} --")

with open("nyse_prices.pickle","wb") as file:
    pickle.dump(df,file)