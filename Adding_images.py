#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 23:16:08 2018

@author: hollyerickson
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fig = plt.figure(figsize=(5,5))
ax1 = fig.add_subplot(1,1,1)

img = mpimg.imread('target.png') # can specify format='png'
ax1.imshow(img)  #Loads as a matrix of points M * N, can also be M * N * 3 (RGB color value), or M * N * 4 (RGBA color value + alpha value)

# plt.savefig('Images/...', orientation='landscape')
plt.show()