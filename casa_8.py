import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

print(df.head())

#for index in df.index:


#print(df['date'][index])
#print(df['iso_a3'][index])
#print(df['currency_code'][index])
#print(df['name'][index])
#print(df['local_price'][index])
#print(df['dollar_ex'][index])
#print(df['dollar_price'][index])
#print(df['USD_raw'][index])
#print(df['EUR_raw'][index])
#print(df['GBP_raw'][index])
#print(df['JPY_raw'][index])
#print(df['CNY_raw'][index])
#print(df['GDP_bigmac'][index])
#print(df['adj_price'][index])
#print(df['USD_adjusted'][index])
#print(df['EUR_adjusted'][index])
#print(df['GBP_adjusted'][index])
#print(df['JPY_adjusted'][index])
#print(df['CNY_adjusted'][index])

#for index in range(len(df)):
    #print(df.loc[index,"name"])
    #df.loc([index,"name"])
    #df.loc([index,"local_price"])
    #df.loc([index,"dollar price"])

#for index in range (len(df)):
    #print(df.iloc[index,0])
    #df.iloc([index,1])
    #df.iloc([index,2])
    #df.iloc([index,3])
    #df.iloc([index,4])
#Method 4 iterrows()

# for i, r in df.iterrows():
#     print(r['date'],r['name'])
#     r['local_price'],r['dollar_price']
# #Method 6  apply()

# print(df.apply(lambda row: row['date'],axis=1))
    


#Method 6