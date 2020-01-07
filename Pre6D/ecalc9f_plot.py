from pylab import *
ion()

g4bl = loadtxt('ecalc9f.dat',skiprows=13)
#icool = loadtxt('ecalc9f_icool.dat',skiprows=13)
#icool[:,1]=icool[:,1]-4.05

titles=['Magnetic field on axis','Transverse emittance','Longitudinal emittance','6D emittance','Average momentum','Transverse beta','Transmission']

close('all')

figure(0)
plot(g4bl[1:,1],g4bl[1:,2]) # Bz
#plot(icool[1:,1],icool[1:,2])
#legend(('G4beamline','ICOOL'))
xlabel('z [m]')
ylabel('Bz [T]')
grid('on')
title('Magnetic field on axis')
#savefig('%s.pdf' % titles[0],dpi=300,bbox_inches='tight')
#savefig('%s.eps' % titles[0],dpi=300,bbox_inches='tight')
savefig('%s.png' % titles[0],dpi=300,bbox_inches='tight')
#savefig('%s.svg' % titles[0],dpi=300,bbox_inches='tight')

figure(1)
plot(g4bl[1:,1],g4bl[1:,3]*1e3) # eperp
#plot(icool[1:,1],icool[1:,3]*1e3)
#legend(('G4beamline','ICOOL'))
xlabel('z [m]')
ylabel('Transverse emittance [mm]')
grid('on')
title('Transverse emittance')
#savefig('%s.pdf' % titles[1],dpi=300,bbox_inches='tight')
#savefig('%s.eps' % titles[1],dpi=300,bbox_inches='tight')
savefig('%s.png' % titles[1],dpi=300,bbox_inches='tight')
#savefig('%s.svg' % titles[1],dpi=300,bbox_inches='tight')

figure(2)
plot(g4bl[1:,1],g4bl[1:,4]*1e3) # elong
#plot(icool[1:,1],icool[1:,4]*1e3)
#legend(('G4beamline','ICOOL'))
xlabel('z [m]')
ylabel('Longitudinal emittance [mm]')
grid('on')
title('Longitudinal emittance')
#savefig('%s.pdf' % titles[2],dpi=300,bbox_inches='tight')
#savefig('%s.eps' % titles[2],dpi=300,bbox_inches='tight')
savefig('%s.png' % titles[2],dpi=300,bbox_inches='tight')
#savefig('%s.svg' % titles[2],dpi=300,bbox_inches='tight')

figure(3)
plot(g4bl[1:,1],pow(g4bl[1:,5]*1e9,1/3.)) # e6d
#plot(icool[1:,1],pow(icool[1:,5]*1e9,1/3.))
#plot(g4bl[1:,1],pow(g4bl[1:,3]*g4bl[1:,3]*g4bl[1:,4]*1e9,1/3.)) # e6d
#legend(('G4beamline','ICOOL'))
xlabel('z [m]')
ylabel('6D emittance [mm]')
grid('on')
title('6D emittance')
#savefig('%s.pdf' % titles[3],dpi=300,bbox_inches='tight')
#savefig('%s.eps' % titles[3],dpi=300,bbox_inches='tight')
savefig('%s.png' % titles[3],dpi=300,bbox_inches='tight')
#savefig('%s.svg' % titles[3],dpi=300,bbox_inches='tight')

figure(4)
plot(g4bl[1:,1],g4bl[1:,7]*1e3) # Pzavg
#plot(icool[1:,1],icool[1:,7]*1e3)
#legend(('G4beamline','ICOOL'))
xlabel('z [m]')
ylabel('Pz_avg [MeV/c]')
grid('on')
title('Average momentum')
#savefig('%s.pdf' % titles[4],dpi=300,bbox_inches='tight')
#savefig('%s.eps' % titles[4],dpi=300,bbox_inches='tight')
savefig('%s.png' % titles[4],dpi=300,bbox_inches='tight')
#savefig('%s.svg' % titles[4],dpi=300,bbox_inches='tight')

figure(5)
plot(g4bl[1:,1],g4bl[1:,8]*1e3) # beta
#plot(icool[1:,1],icool[1:,8]*1e3)
#legend(('G4beamline','ICOOL'))
xlabel('z [m]')
ylabel('beta_perp [mm]')
grid('on')
title('Transverse beta')
#savefig('%s.pdf' % titles[5],dpi=300,bbox_inches='tight')
#savefig('%s.eps' % titles[5],dpi=300,bbox_inches='tight')
savefig('%s.png' % titles[5],dpi=300,bbox_inches='tight')
#savefig('%s.svg' % titles[5],dpi=300,bbox_inches='tight')

figure(6)
plot(g4bl[1:,1],g4bl[1:,12]/g4bl[1,12]) # n0
#plot(icool[1:,1],icool[1:,12]/icool[1,12])
#legend(('G4beamline','ICOOL'))
xlabel('z [m]')
ylabel('Transmission [mm]')
grid('on')
title('Transmission')
#savefig('%s.pdf' % titles[6],dpi=300,bbox_inches='tight')
#savefig('%s.eps' % titles[6],dpi=300,bbox_inches='tight')
savefig('%s.png' % titles[6],dpi=300,bbox_inches='tight')
#savefig('%s.svg' % titles[6],dpi=300,bbox_inches='tight')