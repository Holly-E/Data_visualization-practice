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

#ax1 = fig.add_subplot(2, 1, 1)
#ax2 = fig.add_subplot(2, 1, 2)


axList = [fig.add_subplot(2, 1, num) for num in range(1, 3)]

#note you have to start the axList index at 0 if you do it this way
axList[0].plot(gameNum, HomeTeamGoals, marker='^', c='gray', markerfacecolor='red',linestyle='--', linewidth=1)
axList[1].plot(gameNum, AwayTeamGoals, marker='^', c='green', markerfacecolor='blue',linestyle=':', linewidth=1)

# change x and y limits on axes - FYI plural of axis is axes
#ax1.set_xlim(-1, 145) #could 'flip' graph by setting limits as (145, -1)
#ax1.set_ylim(-1, 7)

# Create tick frequency var, then call var on the axis below, or set directly without creating var
# majorTickLocation = MultipleLocator(10)

# format tick label using python str formatting, ex. add leading zeros if num is less than 3 digits
#majorTickFormat = FormatStrFormatter('%03d')


for ax in axList:
    ax.set_xlim(-1, 145)
    ax.set_ylim(-1, 7)
    # Could add a labelpad=# for distance from label to plot, fontdict with rotation:#, fontsize, color
    ax.set_xlabel('Game Number', labelpad=1)
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.xaxis.set_minor_locator(MultipleLocator(5))
    #ax.xaxis.set_major_formatter(majorTickFormat)

axList[0].set_ylabel('Home Team Goals')
axList[1].set_ylabel('Away Team Goals')

# Format tick label content & rotation
#xTickLabels = axList[1].get_xticks().tolist()
#print(xTickLabels)
xTickLabels = [int(tick) for tick in axList[1].get_xticks().tolist()]
xTickLabels[4] = 'new stadium'
axList[1].set_xticklabels(xTickLabels, rotation= 70)

# To format tick label rotation without changing content 
for xtick in axList[0].get_xmajorticklabels():
    xtick.set_rotation(70)
    
 #can also change title pos with loc='left' or 'right' outside fontdict   
axList[0].set_title('Home Team Goals Over Season', fontdict = {'fontsize': 15, 'color':'red'})
axList[1].set_title('Away Team Goals Over Season', fontdict = {'fontsize': 15, 'color':'blue'})

# ADD tight_layout() to prevent subplots from overlapping
plt.tight_layout()
plt.savefig('Images/lineplot_cust_markers', orientation='portrait')
plt.show()

# USING LATEX in title and x / y labels: .set_title(r'$ latex_code $')