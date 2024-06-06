import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

start_date = '2020-12-1'  
end_date = '2023-2-2'    

# Download data
apple = yf.download(tickers="AAPL",
                    start=start_date,
                    end=end_date)

# Reset index
apple.reset_index(inplace=True)

# Calculate moving average
apple['MA50'] = apple['Close'].rolling(window=50).mean()

# Plot
plt.figure(figsize=(16, 8))
sns.set_style("whitegrid")
sns.lineplot(data=apple, x="Date", y='Close', color='firebrick', label='Close Price')
sns.lineplot(data=apple, x="Date", y='MA50', color='blue', label='50-Day Moving Average')

# Highlight significant dates
significant_dates = {
    '2021-09-14': 'iPhone 13 Launch',
    '2022-01-03': 'Apple Becomes $3 Trillion Company'
}
for date, event in significant_dates.items():
    plt.axvline(pd.to_datetime(date), color='green', linestyle='--', lw=1.5)
    plt.annotate(event, (pd.to_datetime(date), apple['Close'].max()), 
                 xytext=(10,0), textcoords='offset points', 
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

# Customizing the plot
plt.title("The Stock Price of Apple Inc. with 50-Day Moving Average", size=20, color='darkblue')
plt.xlabel("Date", size=14)
plt.ylabel("Stock Price (USD)", size=14)
plt.xticks(size=12, rotation=45)
plt.yticks(size=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.fill_between(apple['Date'], apple['MA50'], apple['Close'], where=(apple['Close'] >= apple['MA50']), facecolor='green', alpha=0.3, interpolate=True)
plt.fill_between(apple['Date'], apple['MA50'], apple['Close'], where=(apple['Close'] < apple['MA50']), facecolor='red', alpha=0.3, interpolate=True)
sns.despine()
plt.legend(fontsize=12)
plt.tight_layout()

# Save the plot
plt.savefig("Apple_Stock_Price_Enhanced.png")

# Show the plot
plt.show()

# Summary of the visualized data
print("Summary of Apple Inc. Stock Price Data:")
print(f"Date Range: {start_date} to {end_date}")
print(f"Initial Closing Price: ${apple['Close'].iloc[0]:.2f}")
print(f"Final Closing Price: ${apple['Close'].iloc[-1]:.2f}")
print(f"Maximum Closing Price: ${apple['Close'].max():.2f} on {apple['Date'][apple['Close'].idxmax()].date()}")
print(f"Minimum Closing Price: ${apple['Close'].min():.2f} on {apple['Date'][apple['Close'].idxmin()].date()}")
