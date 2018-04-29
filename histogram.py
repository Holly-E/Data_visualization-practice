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

plt.style.use('seaborn-whitegrid')


fig = plt.figure(figsize = (7, 5))

ax1 = fig.add_subplot(1, 1, 1)

# HISTOGRAM
ax1.hist((HomeTeamGoals,AwayTeamGoals),
         bins= range(0,8), # default is 10bins, can do int or sequence ex. [0,1,2,3,4,5,6,7] or range
         align='left', #where to align the bins 
         # range = () Will remove outliers based on (start, end)
         color = ('red', 'blue'),
         # cumulative = True Includes the number before it plus itself
         ) 



ax1.set_xlabel('Goals', labelpad=5)


ax1.set_ylabel('Number of Games')


ax1.spines['right'].set_visible(False) 
ax1.spines['top'].set_visible(False)



ax1.set_title('Home Team Goals Over Season', weight='600', fontdict = {'fontsize': 15})


#plt.savefig('Images/histogram', orientation='landscape')
plt.show()

