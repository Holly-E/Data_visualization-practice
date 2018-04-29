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

# Get the Average # goals scored for each team
avgGoalsScoredHome= sum(HomeTeamGoals)/len(HomeTeamGoals)
avgGoalsScoredAway= sum(AwayTeamGoals)/len(AwayTeamGoals)


fig = plt.figure(figsize = (5, 5))
ax1 = fig.add_subplot(1, 1, 1)

# Boxplot - x is defined (Both HTG and ATG are x)
ax1.boxplot([HomeTeamGoals, AwayTeamGoals], sym= '^', #symbols for outliers
           whis = 1.7, #how far whiskers extend, default 1.5, can be a % or 'range' to cover outliers
           # widths = .1, positions = [.5, 3], # width of bars and position along x axis
           notch = True, # confidence interval around median interval (the notches)
           # conf_intervals = [[.9, 1.1], None] #if you know them put them in, or None if you only know for one of the bars
           )

# Change ticks so they make sense        
plt.xticks([1, 2], ['Home Team', 'Away Team'])
ax1.set_ylabel('Goals Scored Per Game')



plt.savefig('Images/boxplot', orientation='portrait')
plt.show()

