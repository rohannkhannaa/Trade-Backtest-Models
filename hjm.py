# Name     : Rohan Khanna
# Email ID : 2020csb1117@iitrpr.ac.in
# Data CopyRight : Futures First


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Step 1: Load Historical Data
data = pd.read_csv('historical_data.csv')
data['Maturity'] = pd.to_datetime(data['Maturity'])  # Convert Date column to datetime format

# Step 2: Define the HJM Model with Constant Volatility
def hjm_model(r, dt, sigma):
    return r + sigma * np.sqrt(dt) * np.random.normal()

# Step 3: Simulate Interest Rate Paths
dt = 1  # quarterly increments
num_paths = 1000  # number of simulated paths
simulated_rates = np.zeros((num_paths, len(data)))
simulated_rates[:, 0] = data['Rate'][0]

constant_volatility = 0.01  # Adjust this value as per your assumption

for i in range(num_paths):
    for j in range(1, len(data)):
        simulated_rates[i, j] = hjm_model(simulated_rates[i, j-1], dt, constant_volatility)

# Step 4: Derive Forward Rates
forward_rates = np.zeros((num_paths, len(data)-1))
for i in range(num_paths):
    for j in range(len(data)-1):
        forward_rates[i, j] = (1 / dt) * (np.exp(simulated_rates[i, j+1] * dt) - 1)

mean_forward_rates = np.mean(forward_rates, axis=0)
maturities = np.arange(1, len(data))

# Step 5: Plot the Forward Curve with Dates on x-axis
plt.plot(data['Maturity'].iloc[:-1], mean_forward_rates)
plt.xlabel('Date')
plt.ylabel('Forward Rate')
plt.title('HJM Model Forward Curve')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent labels from being cut off
plt.show()


# Step 8: Generate Trading Signals
threshold = 0.005  # Threshold for generating trading signals

# Calculate the difference between the current forward rate and the previous forward rate
forward_diff = np.diff(mean_forward_rates)

# Initialize a list to store the trading signals
trading_signals = []

# Generate trading signals based on the forward rate differences
for diff in forward_diff:
    if diff > threshold:
        trading_signals.append("Buy")
    elif diff < -threshold:
        trading_signals.append("Sell")
    else:
        trading_signals.append("Hold")

# Step 9: Print the Trading Signals
for i in range(len(trading_signals)):
    print(f"Signal {i+1}: {trading_signals[i]}")

# Step 10: Backtest the Model
initial_investment = 1000000  # Initial investment amount
portfolio_value = [initial_investment]  # Track portfolio value over time
total_trades = 0  # Track the total number of trades
correct_trades = 0  # Track the number of correct trades

# Calculate daily returns based on actual interest rates
returns = data['Rate'].pct_change()

# Ensure the length of trading signals matches the length of returns
trading_signals = trading_signals[:len(returns)-1]

# Iterate through the returns and calculate the portfolio value
for i in range(1, len(trading_signals)):
    # Calculate the position based on the trading signals
    if trading_signals[i-1] == "Buy":
        position = 1  # Buy position
    elif trading_signals[i-1] == "Sell":
        position = -1  # Sell position
    else:
        position = 0  # No position (Hold)

    # Calculate the portfolio value based on the position and daily return
    portfolio_value.append(portfolio_value[i-1] * (1 + position * returns[i]))

    # Track the number of trades and correct trades
    if position != 0:
        total_trades += 1
        if position == np.sign(returns[i]):
            correct_trades += 1

# Calculate portfolio returns
portfolio_returns = np.array(portfolio_value) / initial_investment - 1

# Calculate buy/sell efficiency
buy_sell_efficiency = correct_trades / total_trades if total_trades > 0 else 0

# Print backtesting results
print("Backtesting Results:")
print(f"Total Return: {portfolio_returns[-1] * 100:.2f}%")
print(f"Annualized Return: {portfolio_returns.mean() * 252 * 100:.2f}%")
print(f"Standard Deviation: {portfolio_returns.std() * np.sqrt(252) * 100:.2f}%")
print(f"Buy/Sell Efficiency: {buy_sell_efficiency * 100:.2f}%")
