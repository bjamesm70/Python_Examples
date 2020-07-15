# Intro.py

# Intro to the "statsmodels" library.

# - Jim


###########
# IMPORTS #
###########

import pandas
import matplotlib.pyplot as plt
import statsmodels.api as sm

########
# CODE #
########

# Sample data provided by "stats models" library:
sample_DF = sm.datasets.macrodata.load_pandas().data

print(sample_DF.info())
print(sample_DF.head())
print("* " * 40)

# Lots of work to set the date to be the index if we
# do it by statsmodels method.  However, it does take in
# quarters as a parameter.  So, it does have its use!

sample_data_index = pandas.Index(sm.tsa.datetools.dates_from_range("1959Q1", "2009Q3"))
sample_DF.index = sample_data_index

print(sample_DF.head())
# print(sample_DF.iloc[0])

sample_DF["realgdp"].plot()
plt.legend()
plt.show()

# Using the "Hodrick-Prescott filter".
# From wikipedia:
# The Hodrick–Prescott filter is a mathematical tool
# used in macroeconomics, especially in real business
# cycle theory, to remove the cyclical component of
# a time series from raw data.
# From me: It shows the overall trend removing the
# mini ups, and downs.  It smooths out the trend.
# Returns a tuple --> (cycle, trend)
# cycle : ndarray --> The estimated cycle in the data given lamb.
# trend : ndarray --> The estimated trend in the data given lamb.
hp_tuple = sm.tsa.filters.hpfilter(sample_DF["realgdp"])

print("* " * 40)
print("Hodrick–Prescott Filter")
print(hp_tuple[0][0], hp_tuple[0][1])
print(type(hp_tuple[0]), type(hp_tuple[1]))

gdp_cycle, gdp_trend = hp_tuple

sample_DF["trend"] = gdp_trend

# sample_DF["realgdp"].plot()
# sample_DF["trend"].plot()
sample_DF[["realgdp", "trend"]].plot()
plt.legend()
plt.show()
