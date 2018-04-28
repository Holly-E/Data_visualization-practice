#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 17:10:28 2018

@author: hollyerickson
"""
import matplotlib.pyplot as plt

# import from ticker to customize axis ticks
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from Goals_Module import AwayTeamGoals
from Goals_Module import HomeTeamGoals

gameNum = [num for num in range(1, len(HomeTeamGoals) + 1)]
print(gameNum)

fig = plt.figure(figsize = (8, 7))
axList = [fig.add_subplot(2, 1, num) for num in range(1, 3)]

# ADD a label which will be the legend after calling .legend()
axList[0].plot(gameNum, HomeTeamGoals, marker='^', c='gray', markerfacecolor='red',linestyle='--', linewidth=1, label='HTG')
axList[1].plot(gameNum, AwayTeamGoals, marker='^', c='green', markerfacecolor='blue',linestyle=':', linewidth=1, label='ATG')


for ax in axList:
    ax.set_xlim(-1, 145)
    ax.set_ylim(-1, 7)
    ax.set_xlabel('Game Number', labelpad=1)
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.xaxis.set_minor_locator(MultipleLocator(5))
    
    # Call legend - label set in .plot()
    ax.legend(loc = 'best') # upper, lower, center, left, right, best

axList[0].set_ylabel('Home Team Goals')
axList[1].set_ylabel('Away Team Goals')


# ADD tight_layout() to prevent subplots from overlapping
plt.tight_layout()
plt.show()

