import pandas as pd
melb_data = pd.read_csv("melb_data.csv")

print(melb_data.groupby(['Suburb','Address','Lattitude','Longtitude']).size())

for i in melb_data.groupby(['Suburb','Address']).size():
    if i > 1:
         print(i)
