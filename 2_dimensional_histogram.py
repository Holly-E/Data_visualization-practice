#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 17:10:28 2018

@author: hollyerickson
"""
import matplotlib.pyplot as plt
from Goals_Module import AwayTeamGoals
from Goals_Module import HomeTeamGoals

#gameNum = [num for num in range(1, len(HomeTeamGoals) + 1)]

#plt.style.use('default')


fig = plt.figure(figsize = (5, 5))

# 2D Histogram (x, y)
plt.hist2d(HomeTeamGoals, AwayTeamGoals, bins=[7, 6], #number of bins for [xbins, ybins]
         )

# If we have no subplots and are only plotting on the plt. can add a colorbar this way:
plt.colorbar()
# After we learn images, we can add the colorbar at the axis level

plt.title('Number of Goals Per Game')
plt.xlabel('Home Team Goals')
plt.ylabel('Away Team Goals')

plt.savefig('Images/2D_histogram', orientation='portrait')
plt.show()

