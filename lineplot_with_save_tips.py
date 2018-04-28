#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 17:10:28 2018

@author: hollyerickson
"""
import matplotlib.pyplot as plt
from Goals_Module import AwayTeamGoals
from Goals_Module import HomeTeamGoals

gameNum = [num for num in range(1, len(HomeTeamGoals) + 1)]
print(gameNum)

plt.figure(figsize = (10, 7))

plt.plot(gameNum, HomeTeamGoals, marker='^', c='gray', markerfacecolor='red',linestyle='--', linewidth=1)
plt.plot(gameNum, AwayTeamGoals, marker='^', c='green', markerfacecolor='blue',linestyle=':', linewidth=1)


#dpi is like resolution. File saved as .png by default, can also save as .pdf by adding it to name.
plt.savefig('Images/lineplot_basic', orientation='landscape', dpi=1000) #higher res = higher file size
plt.show() #show ends the fig, so if you savefig() after you show then nothing will be saved.