#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 17:10:28 2018

@author: hollyerickson
"""
import matplotlib.pyplot as plt
from Goals_Module import AwayTeamGoals
from Goals_Module import HomeTeamGoals

#import 3D toolkit
from mpl_toolkits.mplot3d import Axes3D

gameNum = [num for num in range(1, len(HomeTeamGoals) + 1)]

fig = plt.figure(figsize = (5, 10))

ax1 = fig.add_subplot(2,1,1, projection= '3d') # add 3d projection to subplot
ax2 = fig.add_subplot(2,1,2, projection= '3d')


# 3D line plot (x, y, z)
ax1.plot(gameNum, HomeTeamGoals, AwayTeamGoals, marker='^', c='gray', markerfacecolor='red',linestyle='--', linewidth=1)

ax1.set_xlabel('Game Number')
ax1.set_ylabel('HomeTeamGoals')
ax1.set_zlabel('AwayTeamGoals')
ax1.set_title('3D Line Plot')

# 3D scatter plot (x, y, z), same customization parameters as scatter, plus depthshade to show depth
ax2.scatter(gameNum, HomeTeamGoals, AwayTeamGoals, depthshade = True)
ax2.set_xlabel('Game Number')
ax2.set_ylabel('HomeTeamGoals')
ax2.set_zlabel('AwayTeamGoals')
ax2.set_title('3D Scatter Plot')

# Could make a bunch of subplots of the same graph showing different angles
ax2.view_init(30, 45) #elevation angle (height of camera), rotation angle

# To Animate (If i didn't want to use Plotly)
# Have to update Spyder to 'Automatic' at Preferences > IPython console > Graphics > Graphics Backend
'''
for angle in range(0, 360):
    ax2.view_init(30, angle) # can input any static number or the angle parameter if you want it to change
    plt.draw()
    plt.pause(0.01) #how long you want the animation to hold at each angle
'''
plt.savefig('Images/3D_line_scatter_plots', orientation='landscape')
plt.show() 