# -*- coding: utf-8 -*-
"""Standardization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LSnRtg-sFy2FZQqlsmtE18pd96ro2eK1

#Importing libraries
"""

import numpy as np
import math
import matplotlib.pyplot as plt

#get_ipython().magic('matplotlib.inline')

N=100; #No of observations

#Normal
mu = 40 ;
sigma = 0.5;
X1 = np.random.normal (mu,sigma,N);
X1S = (X1 - mu) / sigma;
print ([np.mean(X1S),np.std(X1S)])

#Exponential
lmda = 10;
X2= np.random.exponential (lmda, N)
X2S= (X2 - lmda)/lmda
print ([np.mean(X2S), np.std(X2S)])

#Uniform
a = -2
b=0
X3 = np.random.uniform (a,b,N);
X3S= (X3-(b+a)/2)/((b-a)**2/12)**(1/2);
print([np.mean(X3S), np.std(X3S)])

y = np.ones (N, dtype=float)
fig, ax= plt.subplots(); ax.set_yticks([])
plt.plot(X1,y, '|r', X2, 2*y, '|g', X3, 3*y, '|b');
plt.show();
#The RGB colors are the 3 observations (100/each)
#Blue for U
#Green for E
#Red for N

#Scaling to see it on a big clear scale
#Every r.v. - mu / sigma = a new value ((X1-mu1)/sigma1) and so on.
#After standardization =>
#mean = ~0
#std = ~1