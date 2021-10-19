#!/usr/bin/env python
# coding: utf-8

# In[94]:


import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-1,1,100)

y = 1/(1+(25*(x**2)))

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r')

# show the plot
plt.show()


# In[13]:


#Fourier
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np


# Number of samplepoints
N = 400
# sample spacing
T = 1 / 800
x = np.linspace(0.0, N*T, N)
y = 1/(1+(25*(x**2)))
xf = np.linspace(0.0, 1.0, N//2)
yf = fft(y)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show()


# In[ ]:




