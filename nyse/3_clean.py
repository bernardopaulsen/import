"""
Title      : Clean Stocks
Description: Removes stocks with less than the maximum data length from dataframe.
Author     : Bernardo Paulsen
Version    : 0.0.1
"""


import pickle


with open("nyse_prices.pickle","rb") as file:
    df = pickle.load(file)


print(len(df.columns))
df = df[1:]
df = df.dropna(1)
print(len(df.columns))


with open("nyse_prices_na.pickle","wb") as file:
    pickle.dump(df,file)