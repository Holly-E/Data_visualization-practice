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