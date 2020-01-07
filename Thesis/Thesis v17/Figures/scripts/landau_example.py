from pylab import *
from scipy.special import expi
close("all")

xmin=-0.5
xmax=5

#figure()
#title("Antiderivative of "+r"$\frac{1-e^{pu}}{u^2}$")
title("Antiderivative of "+r"$(1-e^{pu})/u^2$",fontsize=30)
xlabel(r"$pu$",fontsize=30)
#ylabel(r"$\frac{e^{pu}-1-pu*Ei(pu)}{pu}$")
ylabel(r"$\frac{e^{pu}-1-pu*\mathrm{Ei}(pu)}{pu}$",fontsize=30)
xlim(xmin,xmax)
#yscale('log')
#xscale('log')

x=arange(xmin,xmax,(xmax-xmin)/1000000)
y=[]
for i in range(len(x)):
    y.append((e**x[i]-1-x[i]*expi(x[i]))/x[i])
tight_layout()
plot(x,y)