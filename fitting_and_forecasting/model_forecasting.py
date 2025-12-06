import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#task one - sub sample of data exclusive of last 10 years for training


gold_df = pd.read_csv('/Users/sabiqadar/Desktop/zainab-portfolio/fitting_and_forecasting/gold_price.csv')
gold_df['Date'] = pd.to_datetime(gold_df['Date'])


gold_df = gold_df.sort_values('Date')

# Convert dates to ordinal numbers for polynomial fitting
gold_df['Ordinal'] = gold_df['Date'].map(pd.Timestamp.toordinal)

# Split data into training and testing sets
last_date = gold_df['Date'].max()
cutoff_date = last_date - pd.DateOffset(years=10)

# Training data: all data before cutoff_date
train_df = gold_df[gold_df['Date'] < cutoff_date]
test_df = gold_df[gold_df['Date'] >= cutoff_date]

x_train = train_df['Ordinal'].values
y_train = train_df['Value'].values

# Forecasting over next 10 years
forecast_end = last_date + pd.DateOffset(years=10)
future_dates = pd.date_range(start=last_date, end=forecast_end, freq='MS')
future_ordinals = future_dates.map(pd.Timestamp.toordinal)

#PLOT
plt.figure(figsize=(14, 8))

plt.plot(gold_df['Date'], gold_df['Value'], color='black', label='Actual Price', linewidth=2)

# Fit and plot polynomials of degrees 1 to 9
for deg in range(1, 10):
    # Fit polynomial
    coeffs = np.polyfit(x_train, y_train, deg)
    model = np.poly1d(coeffs)

    # Forecast over future 10 years
    future_pred = model(future_ordinals)

    # Plot forecast
    plt.plot(
        future_dates,
        future_pred,
        label=f'Poly Degree {deg}',
        linewidth=1.5
    )

plt.title("Gold Price Forecasting Using Polynomial Fits (Degrees 1–9)", fontsize=16)
plt.xlabel("Year")
plt.ylabel("Gold Price (USD/oz)")
plt.legend()
plt.grid(True)
plt.show()
