import pandas as pd
data=pd.read_csv("diamonds.csv")
print(pd.Series(data,0.23))