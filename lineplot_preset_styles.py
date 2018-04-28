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

# To view AVAILABLE PRESET STYLES
print(plt.style.available)

# To use a style, note that you can override by specifying colors below
plt.style.use('seaborn-whitegrid') #seaborn-whitegrid I like


fig = plt.figure(figsize = (8, 5))

ax1 = fig.add_subplot(1, 1, 1)

ax1.plot(gameNum, HomeTeamGoals, marker='^',linestyle='--', linewidth=1, label='HTG')

ax1.plot(gameNum, AwayTeamGoals, marker='^',linestyle='--', linewidth=1, label='ATG')

ax1.set_xlim(-1, 145) #could 'flip' graph by setting limits as (145, -1)
ax1.set_ylim(-1, 7)

ax1.set_xlabel('Game Number', labelpad=5)
ax1.xaxis.set_major_locator(MultipleLocator(10))
ax1.xaxis.set_minor_locator(MultipleLocator(5))


ax1.set_ylabel('Home Team Goals')
ax1.legend(loc = 'best')


ax1.spines['right'].set_visible(False) 
ax1.spines['top'].set_visible(False)


ax1.set_title('Home Team Goals Over Season', weight='600', fontdict = {'fontsize': 15})

plt.savefig('Images/lineplot_seaborn-whitegrid', orientation='landscape')
plt.show()

