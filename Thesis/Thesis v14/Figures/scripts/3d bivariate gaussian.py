# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 08:18:40 2016

@author: Josiah D. Kunz
"""
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ion()
rho=0
npart=100 #15000
r=3


x=[]
y=[]
for i in arange(-r,r,r*2./npart):
    for j in arange(-r,r,r*2./npart):
        x.append(i)
        y.append(j)
        
"""
x=2*r*(rand(npart)-1./2)
y=2*r*(rand(npart)-1./2)
"""
sx=np.std(x)
sy=np.std(y)
sx=1.3
sy=sx
z=[]
for i in range(size(x)):
    a=x[i]**2/sx**2-2*rho*x[i]*y[i]/(sx*sy)+y[i]**2/sy**2
    z.append(1/(2*pi*sx*sy*sqrt(1-rho**2))*exp(-a/(2*(1-rho**2))))

x=np.asarray(x)
y=np.asarray(y)
z=np.array(z)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.set_xlim(-r,r)
ax.set_ylim(-r,r)

fontsize=40
xlabel("x",fontsize=fontsize)
ylabel(r"$\theta$",fontsize=fontsize)
plt.setp(ax.get_xticklabels(),fontsize=fontsize/2.)
plt.setp(ax.get_yticklabels(),fontsize=fontsize/2.)
plt.setp(ax.get_zticklabels(),fontsize=fontsize/2.)


#ax.plot_trisurf(x,y,z,alpha=0.5,shade=False)
ax.plot(x,y,z,alpha=0.5)
w=0.07
h=w/3
ax.add_artist(matplotlib.patches.Ellipse((0,-0.033),w,h,angle=7,alpha=0.5,fill=0,color='r'))
show()