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

fig = plt.figure(figsize = (9, 5))
plt.plot(gameNum, HomeTeamGoals, marker='^', c='gray', markerfacecolor='red',linestyle='--', linewidth=1, label='HTG')

# Note if you only have 1 plot (No Subplots) you just do plt.xlim vs axis_name.set_xlim
plt.xlim(-1, 150)
plt.ylim(-1, 7)
plt.xlabel('Game Number', labelpad=1)
plt.ylabel('Home Team Goals')
plt.legend(loc = 'best') # upper, lower, center, left, right, best
plt.title('Home Game Goals 2017')

# TEXT ANNOTATION
# doesn't need .set_ w/ axis, (x,y coord using axis labels, string)
plt.text(40, 4, 'test text', style='oblique', #'italic', 'normal'
         horizontalalignment= 'center', #horiz. align. = center, left, right of text at x coord
         verticalalignment= 'bottom', # bottom, top, center of text at y coord 
         #rotation=45,
         weight = 1000) #range 0 - 1000 (bold)

plt.savefig('Images/lineplot_txt_annotation', orientation='landscape')
plt.show()

