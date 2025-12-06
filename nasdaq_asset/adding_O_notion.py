import pandas as pd
import matplotlib.pyplot as plt
import time

df = pd.read_csv('/Users/sabiqadar/Desktop/zainab-portfolio/nasdaq_asset/HistoricalData_1765051358458.csv',skiprows=1, header = None)
#SAME AS PERVIOUS FILE
#rename columns
df.columns = ['Date', 'Close', 'Volume', 'Open', 'High', 'Low']
#cleaning data by removing $ and making price a float
price_columns = ['Close', 'Open', 'High', 'Low']
for columns in price_columns:
    df[columns] = df[columns].replace('[\$,]', '', regex = True).astype(float)
#convert date column to datetime
df['Date']= pd.to_datetime(df['Date'])
#sort by date
df = df.sort_values("Date")
df = df.reset_index(drop = True)

#addind change in price

df['Daily_Change'] = df['Close'].shift(1)- df['Close']
df = df.dropna(subset=['Close'])

ns = range (7, 365)

for n in ns:
    start_time = time.time()
# O(n) OPERATION - allows us to see linear growth in time taken as n increases
    df_subset = df['Daily_Change'][:n].sort_values()

    end_time = time.time()
    elapsed_time = end_time - start_time

    
#PLOT
plt.figure(figsize=(12,6))
plt.plot(ns, marker='o', linestyle = '-')
plt.xlabel('n(days)')
plt.ylabel('Time taken (seconds)')
plt.title('Big O Notation Analysis')
plt.legend()
plt.grid()
plt.show()
 