# MatPlotLib_Exercises.py

# - Jim

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = x * 2
z = x ** 2

fig1 = plt.figure()
fig1_axes1 = fig1.add_axes([0.1, 0.1, 0.85, 0.85])
fig1_axes1.plot(x, y, "r")

fig1_axes1.set_xlabel("x")
fig1_axes1.set_ylabel("y = x *2")
fig1_axes1.set_title("title")

fig1_axes2 = fig1.add_axes([0.2, 0.5, 0.2, 0.2])
fig1_axes2.plot(x, y, "r")
fig1_axes2.set_xlabel("x")
fig1_axes2.set_ylabel("y = x * 2")

plt.show()

###############################

fig2 = plt.figure()

# Large plot:
fig2_axes1 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])  # Create the axes.
fig2_axes1.plot(x, z)  # Add the graph.
fig2_axes1.set_xlabel("x")
fig2_axes1.set_ylabel("x ** 2")

# Small plot:
fig2_axes2 = fig2.add_axes([0.2, 0.5, 0.4, 0.4])
fig2_axes2.plot(x, y)
fig2_axes2.set_xlabel("x")
fig2_axes2.set_ylabel("x * 2")
fig2_axes2.set_title("Zoom")
fig2_axes2.set_xlim([20, 22])
fig2_axes2.set_ylim([30, 50])

plt.show()

# 2 subplots in 1 figure (1 row, 2 columms):
# Note: If your screen has > 100 per inch, then the output
# will be smaller as dpi defaults to 100.  So, setting
# dpi=115 as per my computer's parameter.
fig3, alist = plt.subplots(1, 2, figsize=(12, 4), dpi=115)

alist[0].plot(x, y, "b--", lw=3)  # Left graph
alist[1].plot(x, z, "r", lw=3)  # Right graph

plt.show()
