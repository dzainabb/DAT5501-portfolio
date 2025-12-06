import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare
import pandas as pd

# Model testing using BIC statistic to find best polynomial degree fit

#FROM PERVIOUS SCRIPTS
#load data
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
# extract training data
x_train = train_df['Ordinal'].values
y_train = train_df['Value'].values

# extract test data (observed values)
x_test = test_df['Ordinal'].values
y_test = test_df['Value'].values

# range of polynomial degrees to test
degrees = range(1, 16)    
bic_values = []
models = []

for deg in degrees:
    # fit polynomial to training data
    coeffs = np.polyfit(x_train, y_train, deg)
    model = np.poly1d(coeffs)
    models.append(model)

    # predictions (expected values)
    y_pred = model(x_test)

    # compute BIC
    rss = np.sum((y_test - y_pred) ** 2)
    n = len(y_test)
    k = deg + 1  # number of parameters

    bic = n * np.log(rss / n) + k * np.log(n)
    bic_values.append(bic)

#higlht best model
best_index = np.argmin(bic_values)
best_degree = degrees[best_index]
best_model = models[best_index]


#plot best model fit against observed data
plt.figure(figsize=(12, 6))
plt.scatter(x_test, y_test, color='black', label='Observed Data', s=20)
plt.plot(x_test, best_model(x_test), color='red', label=f'Best Fit (Degree {best_degree})', linewidth=2)
plt.title(f"Best Model Fit: Polynomial Degree {best_degree}. BIC", fontsize=16)
plt.xlabel("Date (Ordinal)", fontsize=14)
plt.ylabel("Gold Price (USD/oz)", fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
print(f"Best polynomial degree: {best_degree} with BIC values = {bic_values[best_index][0]:.4f}")

