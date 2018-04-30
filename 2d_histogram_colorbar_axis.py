#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 17:10:28 2018

@author: hollyerickson
"""
import matplotlib.pyplot as plt
from Goals_Module import AwayTeamGoals
from Goals_Module import HomeTeamGoals

# Compare to other 2d histogram with colorbar at plt level.


fig = plt.figure(figsize = (5, 5))
ax1 = fig.add_subplot(1, 1, 1)

# 2D Histogram (x, y), set return values w/ tuple unpacking
# counts = 'height' of each square
counts, xedges, yedges, Image = ax1.hist2d(HomeTeamGoals, AwayTeamGoals, bins=[range(8), range(7)]) #specify which color map, many available. _r to reverse

# define edges left, right, top bottom
extent = [xedges[0], xedges[-1], yedges[-1], yedges[0]] #y axis is flipped upside down on images

# cmap moved from ax1.hist2d parameter to im parameter
im = ax1.imshow(counts, extent=extent, cmap = plt.cm.jet) # M * N, or M*N*3 (RGB) or M*N*4 (RGBA - alpha)

#plt.colorbar()
# now save to fig level
fig.colorbar(im, ax = ax1)


# when changing from plt. to ax1. add .set_
ax1.set_title('Number of Goals Per Game')
ax1.set_xlabel('Home Team Goals')
ax1.set_ylabel('Away Team Goals')

plt.savefig('Images/2D_histo_colorbar_with_axis', orientation='portrait')
plt.show()

