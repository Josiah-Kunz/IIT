from pylab import *
import numpy as np
import os.path
ion()
plt.close("all")
bins=50
rcParams["savefig.dpi"]=300
rcParams["figure.figsize"] =8,5

cdata="./cosy/fort.12"
gdata="./g4bl/for009.dat.txt"
idata="./icool/for004.dat"

m=105.6583715
aperture=500

bg=loadtxt(gdata,skiprows=3)
bi=loadtxt(idata,skiprows=2)
#bc=loadtxt(cdata)
# We sometimes get errors in COSY files, esp. when we get > 10^100, since it writes as,
#	e.g., 1.00000001+100 instead of 1.00000001E+100 .
f = open(cdata,'r')
cstr=f.read().splitlines()
f.close()
thc=[]
pc=[]
ec=[]
pyc=[]
thyc=[]
linecounter=0
for line in cstr:
	linecounter+=1
	splitline=line.split()
	try:
		thc.append(1000*arctan(float(splitline[9])/float(splitline[11])))
		pc.append(float(splitline[6])*1000)
		ec.append(1000*sqrt(float(splitline[9])**2+float(splitline[10])**2+float(splitline[11])**2+(m/1000)**2))
		pyc.append(float(splitline[7])*1000)
		thyc.append(1000*arctan(float(splitline[10])/float(splitline[11])))
	except ValueError:
		print("Lost a particle in COSY at line %g!" % (linecounter))

# get rid of NaNs
thg=[]
pg=[]
eg=[]
pyg=[]
thyg=[]
idg=[]
idlast=0
for i in range(0,size(bg[:,9])):
 theta=arctan(bg[i,9]/bg[i,11])*1000
 x=bg[i,6]*1000
 y=bg[i,7]*1000
 e=1000*sqrt(bg[i,9]**2+bg[i,10]**2+bg[i,11]**2+(m/1000)**2)
 thy=arctan(bg[i,10]/bg[i,11])*1000
 idthis=bg[i,0]
 if abs(theta)<1E10 and abs(x)<aperture and e<1E10 and e>0 and abs(y)<aperture and abs(thy)<1E10 and idlast!=idthis: #idg[size(idg)-1]!=idthis:
  thg.append(theta)
  pg.append(x)
  eg.append(e)
  pyg.append(y)
  thyg.append(thy)
  idlast=idthis
  idg.append(idthis)
  
thi=[]
pi=[]
ei=[]
pyi=[]
thyi=[]
idi=[]
idlast=0
for i in range(0,size(bi[:,9])):
 theta=arctan(bi[i,9]/bi[i,11])*1000
 x=bi[i,6]*1000
 y=bi[i,7]*1000
 e=1000*sqrt(bi[i,9]**2+bi[i,10]**2+bi[i,11]**2+(m/1000)**2)
 thy=arctan(bi[i,10]/bi[i,11])*1000
 idthis=bi[i,0]
 if abs(theta)<1E10 and abs(x)<aperture and e<1E10 and e>0 and abs(y)<aperture and abs(thy)<1E10 and idlast!=idthis: #idi[size(idi)-1]!=idthis:
  thi.append(theta)
  pi.append(x)
  ei.append(e)
  pyi.append(y)
  thyi.append(thy)
  idlast=idthis
  idi.append(idthis)

figure(1)
avg=(sum(pg)/len(pg)+sum(pc)/len(pc))/2
lim=min(np.std(pg),np.std(pc))*3
cc,bec=np.histogram(pc,bins,range=(avg-lim,avg+lim)) # Counts COSY, Bin Edges COSY
bcc=(bec[:-1]+bec[1:])/2. # Bin Centers COSY
cg,beg=np.histogram(pg,bins,range=(avg-lim,avg+lim))
bcg=(beg[:-1]+beg[1:])/2.
ci,bei=np.histogram(pi,bins,range=(avg-lim,avg+lim))
bci=(bei[:-1]+bei[1:])/2.
scatter(bcg,cg,label='G4BL',color='green',marker='*')
scatter(bcc,cc,label='COSY',color='red',marker='.')
scatter(bcc,cc,label='ICOOL',color='blue',marker='o')
plt.xlim(avg-lim,avg+lim)
plt.ylim(0,max(max(cc),max(cg))*1.1)
xlabel('X Transverse Position (mm)')
ylabel('Raw Count')
title('X Position Histogram')
legend(loc='upper right')
stdText='G4BL StDev: %3.3f\nCOSY StDev: %3.3f\nICOOL StDev: %3.3f' % (np.std(pg),np.std(pc),np.std(pi))
#stdText='COSY StDev: %g\nG4BL StDev: %g' % (np.std(pc),np.std(pg))
text(plt.gca().get_xlim()[0]*0.95,plt.gca().get_ylim()[1]*0.95, stdText, ha='left', va='top')


figure(2)
#plt.hist(thc,bins,range=[-lim,lim],histtype='step',color='red',label='COSY')
#plt.hist(thg,bins,range=[-lim,lim],histtype='step',color='green',label='G4BL')
#plt.hist(thi,bins,range=[-lim,lim],histtype='step',color='blue',label='ICOOL')
avg=(sum(thg)/len(thg)+sum(thc)/len(thc))/2
lim=min(np.std(thg),np.std(thc))*3
cc,bec=np.histogram(thc,bins,range=(avg-lim,avg+lim)) # Counts COSY, Bin Edges COSY
bcc=(bec[:-1]+bec[1:])/2. # Bin Centers COSY
cg,beg=np.histogram(thg,bins,range=(avg-lim,avg+lim))
bcg=(beg[:-1]+beg[1:])/2.
scatter(bcg,cg,label='G4BL',color='green',marker='*')
scatter(bcc,cc,label='COSY',color='red',marker='.')
#scatter(bci,ci,label='ICOOL',color='blue')
plt.xlim(avg-lim,avg+lim)
plt.ylim(0,max(max(cc),max(cg))*1.1)
xlabel('X Angle (mrad)')
ylabel('Raw Count')
title('X Angle Histogram')
legend(loc='upper right')
stdText='COSY StDev: %3.1f\nG4BL StDev: %3.1f' % (np.std(thc),np.std(thg))
text(plt.gca().get_xlim()[0]*0.95,plt.gca().get_ylim()[1]*0.95,stdText, ha='left', va='top')

figure(4)
avg=(sum(pyg)/len(pyg)+sum(pyc)/len(pyc))/2
lim=min(np.std(pyg),np.std(pyc))*3
cc,bec=np.histogram(pyc,bins,range=(avg-lim,avg+lim)) # Counts COSY, Bin Edges COSY
bcc=(bec[:-1]+bec[1:])/2. # Bin Centers COSY
cg,beg=np.histogram(pyg,bins,range=(avg-lim,avg+lim))
bcg=(beg[:-1]+beg[1:])/2.
scatter(bcg,cg,label='G4BL',color='green',marker='*')
scatter(bcc,cc,label='COSY',color='red',marker='.')
#scatter(bci,ci,label='ICOOL',color='blue')
plt.xlim(avg-lim,avg+lim)
plt.ylim(0,max(max(cc),max(cg))*1.1)
xlabel('Y Position (mm)')
ylabel('Raw Count')
title('Y Position Histogram')
legend(loc='upper right')
#stdText='COSY StDev: %3.3f\nG4BL StDev: %3.3f\nICOOL StDev: %3.3f' % (np.std(pc),np.std(pg),np.std(pi))
stdText='COSY StDev: %g\nG4BL StDev: %g' % (np.std(pyc),np.std(pyg))
text(plt.gca().get_xlim()[0]*0.95,plt.gca().get_ylim()[1]*0.95, stdText, ha='left', va='top')

figure(5)
avg=(sum(thyg)/len(thyg)+sum(thyc)/len(thyc))/2
lim=min(np.std(thyg),np.std(thyc))*3
cc,bec=np.histogram(thyc,bins,range=(avg-lim,avg+lim)) # Counts COSY, Bin Edges COSY
bcc=(bec[:-1]+bec[1:])/2. # Bin Centers COSY
cg,beg=np.histogram(thyg,bins,range=(avg-lim,avg+lim))
bcg=(beg[:-1]+beg[1:])/2.
scatter(bcg,cg,label='G4BL',color='green',marker='*')
scatter(bcc,cc,label='COSY',color='red',marker='.')
#scatter(bci,ci,label='ICOOL',color='blue')
plt.xlim(avg-lim,avg+lim)
plt.ylim(0,max(max(cc),max(cg))*1.1)
xlabel('Y Angle (mrad)')
ylabel('Raw Count')
title('Y Angle Histogram')
legend(loc='upper right')
stdText='COSY StDev: %3.1f\nG4BL StDev: %3.1f' % (np.std(thyc),np.std(thyg))
text(plt.gca().get_xlim()[0]*0.95,plt.gca().get_ylim()[1]*0.95,stdText, ha='left', va='top')

figure(3)
avg=(sum(eg)/len(eg)+sum(ec)/len(ec))/2
lim=3*max(np.std(eg),np.std(ec))
cc,bec=np.histogram(ec,bins,range=(avg-lim,avg+lim)) # Counts COSY, Bin Edges COSY
bcc=(bec[:-1]+bec[1:])/2. # Bin Centers COSY
cg,beg=np.histogram(eg,bins,range=(avg-lim,avg+lim))
bcg=(beg[:-1]+beg[1:])/2.
scatter(bcg,cg,label='G4BL',color='green',marker='*')
scatter(bcc,cc,label='COSY',color='red',marker='.')
#scatter(bci,ci,label='ICOOL',color='blue')
plt.xlim(avg-lim,avg+lim)
plt.ylim(0,max(max(cc),max(cg))*1.1)
xlabel('Final Energy (MeV)')
ylabel('Raw Count')
title('Final Energy Histogram')
legend(loc='upper right')
#stdText='COSY StDev: %3.3f\nG4BL StDev: %3.3f\nICOOL StDev: %3.3f' % (np.std(pc),np.std(pg),np.std(pi))
stdText='COSY StDev: %g\nG4BL StDev: %g' % (np.std(ec),np.std(eg))
text(plt.gca().get_xlim()[0]*1.03,plt.gca().get_ylim()[1]*0.95, stdText, ha='left', va='top')



print("When you're done looking at your data, please hit enter to")
print("exit ths script. Enjoy your day!")
raw_input()
