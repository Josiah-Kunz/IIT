from pylab import *

# reading input data from for003.dat or for004.dat
b=loadtxt('for004.dat',skiprows=3)

# saving data to for009.dat for ecalc9
c=zeros((b.shape[0],23))
c[:,0:4]=b[:,0:4]
c[:,4]=1 # artificial region (JSRG) number
c[:,5]=b[:,4] # time
c[:,6:12]=b[:,6:12] # coordinates are the same in for009 and for003
#c[:,8]=0 # except for z that we change to zero
c[:,12:15]=zeros((b.shape[0],3)) # three zeros, since no information in for003
c[:,15]=b[:,5] # stat weight
c[:,16:20]=zeros((b.shape[0],4)) # four zeros, no information for003
c[:,20:23]=b[:,12:15] 
dest=open('for009_from_for004.dat','w')
dest.write('# for009 output generated from for004\n')
dest.write('# units = [s] [m]  [GeV/c] [T] [V/m]\n') 
dest.write('# evt par typ flg reg time x y z Px Py Pz Bx By Bz wt Ex Ey Ez arclength polX polY polZ\n')

for line in c:
  dest.write('%i %i %i %i %i %g %g %g %g %g %g %g %g %g %g %g %g %g %g %g %g %g %g\n'%tuple(line))

dest.close()
