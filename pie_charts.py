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


totalGoalsScoredHome= sum(HomeTeamGoals)
totalGoalsScoredAway= sum(AwayTeamGoals)


fig = plt.figure(figsize = (5, 5))
ax1 = fig.add_subplot(1, 1, 1)

# Pie chart - if sum of values is > 1, chart will be normalized to a fraction x[i]/sum(x)
# if sum of values < 1, chart will be missing a segment
ax1.pie([totalGoalsScoredHome, totalGoalsScoredAway, 200], labels=['Home Team', 'Away', 'Other'],
        labeldistance= 1.1, #default distance from center 1.1
        colors= ['red', 'blue', 'black'],
        explode = [0, .1, 0], #pops out part of chart, each value corresponds to index of x
        shadow = True,
        radius = 1.1, # default radius is 1
        #center = [1,2] #default is [0,0], when overlayed on another plot
        )

ax1.set_title('Goals Over Season', weight='600', fontdict = {'fontsize': 15})

plt.savefig('Images/piechart', orientation='landscape')
plt.show()

