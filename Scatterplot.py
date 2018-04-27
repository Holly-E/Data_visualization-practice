# -*- coding: utf-8 -*-
"""
Spyder Editor

Master Data Visualization with Python Course
"""
import matplotlib.pyplot as plt

with open('Goals.txt', 'r') as goalData:
    homeTeamLine = goalData.readline()
    
    #remove trailing line break
    homeTeamLine = homeTeamLine.strip('\n')
    
    #txt only contains str so turn into array of integers
    homeTeamLine = homeTeamLine.split()
    HomeTeamGoals = [int(x) for x in homeTeamLine]
    
    
    awayTeamLine = goalData.readline()
    
    #remove trailing line break
    awayTeamLine = awayTeamLine.strip('\n')
    
    #txt only contains str so turn into array of integers
    awayTeamLine = awayTeamLine.split()
    AwayTeamGoals = [int(x) for x in awayTeamLine]
 
print(HomeTeamGoals)    
print(AwayTeamGoals)

# The figure is the frame, the graph is a plot that is put onto the frame
# not necessary to do this step (figure created automatically), unless wanting to adjust the figure
plt.figure(figsize = (9, 5), facecolor='blue')

# By default the most recent figure created is used, you can switch between them by naming them
fig1 = plt.figure('wide', figsize = (10, 5))
fig2 = plt.figure('tall', figsize = (5, 10))

#call using name
plt.figure('tall')

# Scatter plot can show what values occured, ex. (1, 1) but not how many of those values
# s = dot size, c = color, marker = symbol, alpha = transparency
plt.scatter(HomeTeamGoals, AwayTeamGoals, s=40, c='orange', marker='^', alpha = .3)

#switch figure
plt.figure('wide')

plt.scatter(HomeTeamGoals, AwayTeamGoals, s=40, c='black', marker='^', alpha = .3)
plt.show()