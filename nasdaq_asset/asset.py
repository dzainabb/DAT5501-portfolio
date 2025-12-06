import pandas as pd
import matplotlib.pyplot as plt

asset_data = pd.read_csv('/Users/sabiqadar/Desktop/zainab-portfolio/nasdaq_asset/HistoricalData_1765051358458.csv',skiprows=1, header = None)

#rename columns
asset_data.columns = ['Date', 'Close', 'Volume', 'Open', 'High', 'Low']

#cleaning data by removing $ and making price a float

price_columns = ['Close', 'Open', 'High', 'Low']

for columns in price_columns:
    asset_data[columns] = asset_data[columns].replace('[\$,]', '', regex = True).astype(float)

#convert date column to datetime

asset_data['Date']= pd.to_datetime(asset_data['Date'])

#plotting closing price over time
asset_data = asset_data.sort_values("Date")

asset_data = asset_data.reset_index(drop = True)

#PLOT
plt.figure(figsize=(12,6))
plt.plot(asset_data['Date'], asset_data['Close'], label='Closing Price')
plt.xlabel('Date')
plt.ylabel(' Closing Price ($)')
plt.title('Closing Price Over Time')
plt.legend()
plt.grid()
plt.show()

#percentage change 

asset_data['%_change'] = asset_data['Close'].pct_change()

#PLOT

plt.figure(figsize=(12,6))
plt.plot(asset_data['Date'], asset_data['%_change'])
plt.xlabel('Date')
plt.ylabel('Percentage Change')
plt.title('Percentage Change in Closing Price Over Time')
plt.legend()
plt.grid()
plt.show()

#ADDING IN MOVING AVERAGE

asset_data['MA_20'] = asset_data['Close'].rolling(window=20).mean()
asset_data['MA_50'] = asset_data['Close'].rolling(window=50).mean()

#PLOT

plt.figure(figsize=(12,6))
plt.plot(asset_data['Date'], asset_data['Close'], label='Closing Price')
plt.plot(asset_data['Date'], asset_data['MA_20'], label='20-Day MA')
plt.plot(asset_data['Date'], asset_data['MA_50'], label='50-Day MA')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.title('Closing Price with Moving Averages')
plt.legend()
plt.grid()
plt.show()

