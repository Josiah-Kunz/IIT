from pylab import *

b=loadtxt('for009_all.dat')

ind = b[b[:,4]==138,0] # surviving muons indices, after 3 m, regn 84; 5 m, regn 138
#ind = b[b[:,4]==b[-1,4],0] # surviving muons indices
result = b[in1d(b[:,0],ind),:] # only the rows of b corresponding to survivors

dest=open('for009.dat','w')
dest.write('# Good muons only\n')
dest.write('#  units = [s] [m]  [GeV/c] [T] [V/m]\n')
dest.write('#  evt par typ flg reg time x y z Px Py Pz Bx By Bz wt Ex Ey Ez arclength polX polY polZ\n')

for line in result:
  dest.write('%i %i %i %i %i %g %g %g %g %g %g %g %g %g %g %g %g %g %g %g %g %g %g\n'%tuple(line))

dest.close()


