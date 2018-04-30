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

print(plt.style.available)
plt.style.use('default') 

fig = plt.figure(figsize = (5, 4))
ax1 = fig.add_subplot(1, 1, 1)

# When working with bars, etc. vs matrix:
# Get the cmap colors, then save each color in the cmap (within the maximum) to colors
cmap = plt.cm.get_cmap('ocean', 8) # name, Number to assign maximum
colors = cmap(range(8)) #[0, 1, 2, 3...] array of corresponding colors

#axes actually return values we can capture; n = value of each bin, bins = edges of bins, patches = bin object themselves
n, bins, patches = ax1.hist((HomeTeamGoals), bins= range(8)) 

# Can skip this step if you don't care if color has significance
patchHeights =[[patch, patch.get_height()] for patch in patches]
sortHeights = sorted(patchHeights, key=lambda patch: patch[1]) 
patchesSorted = []
for obj in sortHeights:
    patchesSorted.append(obj[0])

# zipping will zip the colors and patches list together and go through one by one and store each variable as color, patch simultaneously. Same as doing:
# for i in range(len(colors)):
    # color = colors[i]
    # patch = patches[i]
for color, patch in zip(colors, patchesSorted): # or (colors, patches) if you aren't coloring by height
    patch.set_facecolor(color)

ax1.set_xlabel('Goals', labelpad=5)
ax1.set_ylabel('Games')
ax1.set_title('Home Team Goals Over Season', weight='600')


#plt.savefig('Images/histogram_colormapped', orientation='landscape')
plt.show()

