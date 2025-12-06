import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
#model testoing - which model fits best 

#load in the dataset
gold_df = pd.read_csv ('/Users/sabiqadar/Desktop/zainab-portfolio/fitting_and_forecasting/gold_price.csv')
gold_df.head(3)

#make date in datetime format
gold_df['Date'] = pd.to_datetime(gold_df['Date'])

#get an average of year golf prices
average_prices = gold_df.groupby(gold_df['Date'].dt.year)['Value'].mean().reset_index()
average_prices.columns = ['Year', 'Average_Price']

# polynomial fit
x = average_prices['Year']
y = average_prices['Average_Price']


coefficients= np.polyfit(x,y, 9, w=None)
p = np.poly1d(coefficients)
 
# PLOT
plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=10, label='Actual Data')
plt.plot(x, p(x), color='red', label='Polynomial Fit (deg=9)')
plt.xlabel('Date')
plt.ylabel('Gold Price - per ounce (USD)')
plt.title('Gold Price Polynomial Trend')
plt.legend()
plt.show()

