# ETS.py

# Errors, Trends, and Seasonality analysis
# for airline travelers.

# Note: At the time of this writing (2020-07-14), there is
# a problem with the latest version of "matplotlib" (3.3.0.rc1)
# when trying to plot the seasonal_decompose graph (w/ all
# its sub-graphs: Trends, Seasonality, and Errors).  They
# all show up as blank.
# So, just use the version that pycharm recommends at this
# time: 3.2.2.

# - Jim

import pandas
import matplotlib.pyplot as plt

# For getting the ETS data.
from statsmodels.tsa.seasonal import seasonal_decompose

airline_DF = pandas.read_csv("./airline_passengers.csv", index_col="Month")

# print(airline_DF.head())
# print(airline_DF.info())

# Removing missing values:
airline_DF.dropna(inplace=True)
# print(airline_DF.info())

# Convert the index to DateTime objects.
airline_DF.index = pandas.to_datetime(airline_DF.index)

print(airline_DF.head())
airline_DF.plot()
plt.show()

# # If the graph is linear, use: model="additive".
# # If the graph is a curve, use: model="multiplicative".

result = seasonal_decompose(airline_DF['Thousands of Passengers'], model='additive')
result.plot()
plt.show()

result = seasonal_decompose(airline_DF['Thousands of Passengers'], model='multiplicative')
result.plot()
plt.show()
