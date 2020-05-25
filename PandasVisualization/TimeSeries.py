# TimeSeries.py

# - Jim

import pandas
import matplotlib.pyplot as plt  # REQUIRED!
from matplotlib import dates  # For prettying data on graphs.

# parse_dates --> See if any of the data can be converted to datetimes.
# Do so if the whole column is made of datetimes.
mc_data = pandas.read_csv("mcdonalds.csv", index_col="Date", parse_dates=True)

print(mc_data)

mc_data['Adj. Close'].plot(title="Close Price",
                           xlim=["2007-01-01", "2009-01-01"],
                           ylim=[0, 80],
                           color="orange",
                           figsize=(10, 4))
plt.show()

mc_data["Adj. Volume"].plot(title="Volume", figsize=(12, 4))
plt.show()

# A slice of a DF, and then get the "index" values for the table:
# Note: however, it looks like "slicing" a DF includes the upper
# bound, which is not how normal slicing works.
mc_index = mc_data.loc["2007-01-01":"2007-05-01"].index

# We just want the "Adj. Close" column from this subset:
# (Note: The will still have its index included w/ its data.)
mc_cprice = mc_data.loc["2007-01-01":"2007-05-01"]["Adj. Close"]

print("-" * 40)
print(mc_index)
print(mc_cprice)

# Creating just the 1 subplot w/i the figure.
figure, axes = plt.subplots()
axes.plot_date(mc_index, mc_cprice, "-")

# The dates, on the x-axis, are overlapping.
# Clean it up with: autofmt_xdate()
# Notes:
# 1) It causes the dates to be printed at an angle.
# 2) The command is associated with the figure not the axes (weird).
figure.autofmt_xdate()

# Dividing the x-axis labels up i/2 2 sections:
# major ticks: with mon-year
# minor ticks: with day of month.

# major label:
# Only print Year, and Month for the date: YYYY-MM
axes.xaxis.set_major_locator(dates.MonthLocator())  # Find the months in the x-axis data.
axes.xaxis.set_major_formatter(dates.DateFormatter("\n\n%b-%Y"))  # Format as: Apr-2007
# Also the "\n\n" moves the major labels down by 2 lines.

# minor label:
# WeekdayLocator() --> Only grab data from 1 day of the week:
# byweekday=5 --> 0=Monday, 6=Sunday, default = 1 = Tuesday
# 5=Saturday --> So data defaults to a complete week.
axes.xaxis.set_minor_locator(dates.WeekdayLocator(byweekday=5))
axes.xaxis.set_minor_formatter(dates.DateFormatter("%d"))

# Add it grid lines for y axis:
axes.yaxis.grid(True)

plt.show()
