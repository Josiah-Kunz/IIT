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
npart=10000 #15000
r=4


x=[]
y=[]
means=[0,0]
cov=[[1.3,0],[0,1.3]]
for i in arange(-r,r,r*2./npart):
    a,b=np.random.multivariate_normal(means,cov)
    x.append(a)
    y.append(b)
        
"""
x=2*r*(rand(npart)-1./2)
y=2*r*(rand(npart)-1./2)
"""

x=np.asarray(x)
y=np.asarray(y)
fig=plt.figure(figsize=(15,10))
ax=fig.add_subplot(111,projection='rectilinear')
ax.set_xlim(-r,r)
ax.set_ylim(-r,r)
ax.scatter(x,y,alpha=0.5)

fontsize=40
title(r"x-$\theta$ phase space",fontsize=fontsize)
xlabel("x (cm)",fontsize=fontsize)
ylabel(r"$\theta$ (mrad)",fontsize=fontsize)
plt.setp(ax.get_xticklabels(),fontsize=fontsize/2.)
plt.setp(ax.get_yticklabels(),fontsize=fontsize/2.)

x=np.linspace(-r,r,npart/10)
y=np.linspace(-r,r,npart/10)
x,y=np.meshgrid(x,y)
sx=cov[0][0]
sy=cov[1][1]
sxy=cov[0][1]
CS=plt.contour(x,y,((x**2*sy**2-2*x*y*sxy+y**2*sx**2)/(2*(sx**2*sy**2-sxy**2))-1),[0],colors='red')
plt.setp(CS.collections[0],linewidth=4)
#ax.add_artist(matplotlib.patches.Ellipse((0,-0.033),w,h,angle=7,alpha=0.5,fill=0,color='r'))
show()