import pandas as pd


data_list = ['Bitcoin','Cardano', 'Ethereum', 'LUNA', 'USDT']

data_merge = pd.DataFrame(columns=['Date', 'Price', 'daily_volume', 'type'])
data_output = []    
for i in data_list:
    try:
        data = pd.read_csv('./prices_data/'+i+'.csv')
    except:
        print("error reading file")
        
    df = pd.concat([data[['Date', 'Price', 'daily_volume']]])
    df['type'] = i
    out = df.to_json(i, orient="records")
    
    data_merge=pd.concat([data_merge, df], axis=0)
    
    
    # data_output.append(df)
    
# data_csv = pd.DataFrame(data_output, columns=['Date', 'Price', 'Vol'])
# print(data_csv) 

print(data_merge)

outin = data_merge.to_csv("general_prices.csv" , index=False)

