# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 21:24:56 2022

Answering the question from Dr. Pavlov:
Given: the curve of the body midline of swimming tuna.
Question: What would be an expression to place 20 points at equal interval 
50.2 mm along this curve?

Inputs: an x by 2 array of the curve of the tuna (curve of x and y)
Outputs: 1)Graph of original xy points (blue) and equally spaced points (red)
    2) csv file of the xy locations of the equally spaced curves for future
    analysis (evenpoints.csv)
Use: Generate n number of equally spaced points along the curve of the 
tuna midline

@author: markl
"""

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

#tuna midline curve (input)
curve = '''0   -16.1
    54   -14.1
    108   -12.1
    162   -10.5
    216   -9.4
    270   -8.7
    324   -8.4
    378   -8.3
    432   -8.0
    486   -7.3
    540   -5.6
    594   -2.8
    648   1.7
    702   7.9
    756   16.1
    810   26.3
    864   38.4
    918   51.9
    972   66.4
    1026   81.3
    1080   95.8'''

#process data
curve = np.array([line.split() for line in curve.split('\n')],dtype=float)

x,y = curve.T
xd = np.diff(x)
yd = np.diff(y)
dist = np.sqrt(xd**2+yd**2) #distance between each of the points
u = np.cumsum(dist)
u = np.hstack([[0],u])

n = 20 # number of new points along the curve (CAN BE EDITED)

#create new x and y points (evenly space along curve)
t = np.linspace(0,u.max(),n)
xn = np.interp(t, u, x)
yn = np.interp(t, u, y)


#plot new (even) points along the curve of old xy points 
f = plt.figure()
ax = f.add_subplot(111)
#ax.set_aspect('equal') #uncomment/comment this to show the true size of the graph/distance between points
ax.plot(x,y,'o', alpha=0.3)
ax.plot(xn,yn,'ro', markersize=8, alpha=0.3)
ax.set_xlim(0,1200) #CAN BE EDITED FOR DIF MAX VALUES OF X
plt.title('Body Midline')
ax.legend(['Original','Even spaced'])
ax.set_xlabel('mm')
ax.set_ylabel('mm')


#export new (even) points
evenpts = np.stack((xn, yn), axis = 1)
pd.DataFrame(evenpts).to_csv('evenpoints.csv')

