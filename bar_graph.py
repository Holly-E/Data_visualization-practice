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

# Get the Average # goals scored for each team
avgGoalsScoredHome= sum(HomeTeamGoals)/len(HomeTeamGoals)
avgGoalsScoredAway= sum(AwayTeamGoals)/len(AwayTeamGoals)


fig = plt.figure(figsize = (5, 5))
ax1 = fig.add_subplot(1, 1, 1)

# Bar Graoh - instead of x and y, we have left and height. The heights are plotted at the left values, can have more than 2
ax1.bar(left = [1, 2], height = [avgGoalsScoredHome, avgGoalsScoredAway],
        width = .5, # defaul bar width is 0.8
        align = 'center', # center or edge
        color = ['red', 'blue'],
        #bottom = [0, avgGoalsScoredHome] starting point for bottom of each bar. Can actually have bars share same left position to stack them
        ) 

# Change ticks so they make sense        
plt.xticks([1, 2], ['Home Team', 'Away Team'])

# Change limits to make it look zoomed out
ax1.set_ylim(0, 2)
ax1.set_xlim(.25, 2.75)

ax1.set_ylabel('Average Goals Scored')
ax1.set_title('Home Team Goals Over Season', weight='600', fontdict = {'fontsize': 15})


plt.savefig('Images/bar_graph', orientation='portrait')
plt.show()

