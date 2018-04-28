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

plt.plot(gameNum, HomeTeamGoals, marker='^', c='gray', markerfacecolor='red',linestyle='--')
plt.plot(gameNum, AwayTeamGoals, marker='^', c='green', markerfacecolor='blue',linestyle=':')
plt.show()