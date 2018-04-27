# -*- coding: utf-8 -*-
"""
Spyder Editor

Master Data Visualization with Python Course
"""
import matplotlib.pyplot as plt
from Goals_Module import AwayTeamGoals
from Goals_Module import HomeTeamGoals

fig1 = plt.figure(figsize = (8, 5))

# create subplots (axis are the blank canvases on the frame)
ax1 = fig1.add_subplot(3, 2, 2) #nrows, ncolumns, index (between 1 and nrows * ncolumns)
ax2 = fig1.add_subplot(3, 1, 2) #note the nrows and ncolumns don't have to be the same
ax3 = fig1.add_subplot(3, 3, 8)

# change plt to the axis name to set which axis you will use
ax2.scatter(HomeTeamGoals, AwayTeamGoals, s=40, c='blue', alpha = .3)


# can also loop through the axis to create them
fig2 = plt.figure()
axList = []

for ax in range(1, 10):
    axList.append(fig2.add_subplot(3, 3, ax))
 
# can now select axis using index of axList
axList[4].scatter(HomeTeamGoals, AwayTeamGoals, s=40, c='red', alpha = .3)
plt.show()  