# PandasVisualizationIntro.py

# Pandas Visualization Intro

# - Jim

import numpy
import pandas
import matplotlib.pyplot as plt  # REQUIRED!

# pandas' visualization is built on top of matplotlib!

DF1 = pandas.read_csv("df1.csv", index_col=0)
DF2 = pandas.read_csv("df2.csv")

print(DF1.head())
print(DF2.head())

# DF1["A"].hist(bins=30)
DF1["A"].hist()

plt.show()  # Required for showing Pandas' graphs!

# DF1["A"].plot(kind="hist")
DF1.plot(kind="hist", alpha=0.4)
DF2.plot.area(alpha=0.5)
DF2.plot.bar()
DF2.plot.bar(stacked=True)

plt.show()

# Line plots:
DF1.plot.line(y="B")

plt.show()

# Scatter plots:
# 2nd with using column "C" as the color heat map -> black & white.
# 3rd with using column "C" as the color heat map -> w/ predefined color scheme.

DF1.plot.scatter(x="A", y="B")
DF1.plot.scatter(x="A", y="B", c="C")
DF1.plot.scatter(x="A", y="B", c="C", cmap="coolwarm")

# Adjust size of each dot based off of column "C".
# "s=" for "scale".
# However, in python 3.8, it throws an error (but produces
# the chart).  Error:
# RuntimeWarning: invalid value encountered in sqrt
#   scale = np.sqrt(self._sizes) * dpi / 72.0 * self._factor
# Error is due to :
# the "scaling" taking the square root of everything
# in column "C" including the negative values.
# So, as a work around, I am adding in "abs()
DF1.plot.scatter(x="A", y="B", s=abs(DF1["C"] * 10), title="Scatter w/ Weighting")

plt.show()

# Box plot:
# I read the definition of a box plot at:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.boxplot.html
# It does not make sense to me (at this point)  as it does not match up with
# the graph.
DF2.plot.box()
plt.show()

# ***** #

# Hex plots: It's basically a scatter plot w/ hexes.
# randn --> random normalized = Bell Curve.
DF3 = pandas.DataFrame(numpy.random.randn(1000, 2), columns=['a', 'b'])
print(DF3.head())

# DF3.plot.hexbin(x="a", y="b", gridsize=25, cmap="coolwarm", title="Hex Bin")
DF3.plot.hexbin(x="a", y="b", gridsize=25, title="Hex Bin")

plt.show()

# Kernel Density Estimate Plot = Probability Chart
# If you have normalized data, graph will show up as a Bell Curve.
DF3["a"].plot.kde()  # Bell Curve
DF3.plot.kde()

plt.show()
