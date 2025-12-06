# fitting_and_forcasting

Task:
Dataset that analyses global trend over 100 years. 
Trend of choice : Gold Price

This project explores gold price forecasting using polynomial regression models. The dataset is split into training and testing sets, excluding the last 10 years for training, and then forecasting is performed for the next 10 years. Models of polynomial degrees 1–9 are fitted and compared, with evaluation using Bayesian Information Criterion (BIC) and Chi-Squared tests.

Features
Load and preprocess historical gold price data.
Train polynomial regression models of varying degrees.
Forecast gold prices for the next 10 years.
Visualize actual vs. forecasted prices.
Evaluate models using:
Bayesian Information Criterion (BIC) for model selection.
Chi-Squared test for goodness-of-fit.
