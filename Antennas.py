# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

"""
stuff you will find useful dealing with antennas
"""

from math import *
# some constants
c=2.998e8 # velocity of light in m/s
k=1.38e-23 # Boltzmann constant in J/K
Jy=1e-26 #W/m**2/Hz

def dB(G):
    # give a gain and return decibel version
    B=log10(G)
    db=10*B
    return(db)

def S(T,freq,omega):
    # give a flux density from source brightness temp, frequency and solid angle
    B=2*kT*freq**2/c**2 # 
    s=B*omega # still in MKS units W/m**2/Hz
    return(s)
    

# <codecell>

#Observe a source at 1.8GHz with a 12m dish
freq=1.88e9  # Hz
diameter=12.0 # m
area=pi*diameter**2/4.0 #m**2
wavel=c/freq        # in m
HPBW=wavel/diameter # in radians
print degrees(HPBW),"degrees"
print area,diameter,wavel,HPBW

# <codecell>

#actual efficiency about 70% - mostly taper
Ae=area*0.7 #m**2
omega_a=wavel**2/Ae
gain=4*pi/omega_a # Gain along pointing axis
hpbw=sqrt(omega_a*4/pi)
print omega_a,gain,Ae,hpbw
print degrees(hpbw)

# <codecell>

#Note that reducing efficiency WIDENS beam 

# <codecell>

"""
We can also express antenna gain in K/Jy
from How many K we would get for a 1Jy in front of it
"""
KperJy=Ae*1*Jy/(2*k)
print KperJy

# <codecell>

"""
Other measurements of sensitivity need system temperature measurements
"""
Tsys=30
SEFD = Tsys/KperJy  # System Equivalent Flux Density
# This represents how many Jy to equal system temperature
print "Ae/Tsys",Ae/Tsys,"m**2/K    SEFD",SEFD,"Jy"

# <codecell>


