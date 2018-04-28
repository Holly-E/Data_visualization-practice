#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 17:10:28 2018

@author: hollyerickson
"""
import matplotlib.pyplot as plt

# import from ticker to customize axis tick spacing
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from Goals_Module import AwayTeamGoals
from Goals_Module import HomeTeamGoals

gameNum = [num for num in range(1, len(HomeTeamGoals) + 1)]
print(gameNum)

fig = plt.figure(figsize = (8, 5))

ax1 = fig.add_subplot(1, 1, 1)

ax1.plot(gameNum, HomeTeamGoals, marker='^', c='gray', markerfacecolor='red',linestyle='--', linewidth=1, label='HTG')


ax1.set_xlim(-1, 145) #could 'flip' graph by setting limits as (145, -1)
ax1.set_ylim(-1, 7)

ax1.set_xlabel('Game Number', labelpad=1)
ax1.xaxis.set_major_locator(MultipleLocator(10))
ax1.xaxis.set_minor_locator(MultipleLocator(5))


ax1.set_ylabel('Home Team Goals')
ax1.set_ylabel('Away Team Goals')
ax1.legend(loc = 'upper left')

# Customize SPINE visibility
ax1.spines['right'].set_visible(False) #bottom, right, top, left
ax1.spines['top'].set_visible(False)

#To specify which sides DO have tick marks
ax1.yaxis.set_ticks_position('left') #left, right or for xaxis: bottom, top

#To completely remove all ticks, set to an empty list:
#ax1.yaxis.set_ticks([]) or ax1.xaxis...

ax1.set_title('Home Team Goals Over Season', fontdict = {'fontsize': 15})

plt.show()

