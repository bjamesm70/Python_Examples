# Walmart_Bollinger_Bands.py

# Create Bollinger Bands (by hand) from Walmart daily data.
# I am not finding a predefined Pandas function for this.

# I could add more to this: making the Bollinger Bands
# dashed lines, for example.

# - Jim

# import numpy  # Not used.
import pandas
import matplotlib.pyplot as plt

# Import the Walmart data converting the "Date" column to the index, and as DateTimes.
Walmart_DF = pandas.read_csv("./walmart_stock.csv", index_col="Date", parse_dates=True)

# Get a look at the daily chart by itself.

Walmart_DF['Close'].plot(figsize=(16, 6), title="Walmart Close Prices")
plt.show()

# Creating "Bollinger Bands" by hand.
# (I am surprised there is no way predefined function in Pandas.)

# Close:
# Already given as Walmart_DF["Close"]

# Close 20 SMA:
Walmart_DF["Close: 20 SMA"] = Walmart_DF["Close"].rolling(20).mean()

# Upper = 20SMA + 2*std(20)
Walmart_DF["Upper"] = Walmart_DF["Close: 20 SMA"] + \
                      2 * (Walmart_DF["Close"].rolling(20).std())

# Lower = 20SMA -2 *std(20)
Walmart_DF["Lower"] = Walmart_DF["Close: 20 SMA"] - \
                      2 * (Walmart_DF["Close"].rolling(20).std())

Walmart_DF[["Close",
            "Close: 20 SMA",
            "Upper",
            "Lower"]].plot(figsize=(16, 6), title="Walmart Stock Prick With Bollinger Bands")
plt.show()
