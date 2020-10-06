
# coding: utf-8

# In[1]:


"""
Odd formulae
To do with sensitivity, beam etc,
"""
import math as m

lat=-30.7 #degrees south

slat=m.sin(m.radians(lat))
clat=m.cos(m.radians(lat))
#

dec=-50.
ha=-33.

sdec=m.sin(m.radians(dec))
cdec=m.cos(m.radians(dec))
cha=m.cos(m.radians(ha))
sha=m.sin(m.radians(ha))
#print clat,slat,sdec,cdec,cha,sha


# In[2]:


parallac=m.atan2(sha*clat,(cdec*slat-sdec*clat*cha))
x=sdec*slat+cdec*cha*clat
elev=m.asin(x)
az=cdec*sha/m.sqrt(1-x*x)
#az=(elev-sdec*slat)/(cdec*clat)
az=az+m.pi
print (m.degrees(parallac), m.degrees(elev), m.degrees(az))
print ("Azimuth {0:6.3f} Elevation {1:6.3f} Parallactic angle {2:6.3f}".format(m.degrees(az),m.degrees(elev),m.degrees(parallac)))


# In[3]:


min=20. #minimum elevation

smin=m.sin(m.radians(min))
y=(smin-sdec*slat)/(cdec*clat)
#print y
if y <1.0 and y > -1.0:
    amin=m.acos(y)
    print ("Minimum elevation reached at HA {0:6.1f}".format(m.degrees(amin)))
    print ("Total time up {0:6.1f}hr".format((m.degrees(amin))*2/15))
else:
    print("Circumpolar")


# In[34]:


"""
Bandwidth,integration, baselines, freq
delay beams, fringe beams

"""
# a few constants
ar= 3600*m.degrees(1) #arcseconds per radian - about 206265
day=23.9344696*3600 # sideral day in sec
c=299792.458 #km/s
#print ar,day,c



bw=544./1024 #MHz
t=8. #sec
#d=7.6 #km
f=0.85 #GHz


lam=0.0001*c/f #wavelength/cm

d=lam/10 # 1kilolambda

res=lam*0.00001*ar/d  #arcsec
print ("Wavelength {0:6.2f}cm  \t resolution {1:6.2f}arcsec".format(lam,res))
print("1kl is {0:6.3f}km".format(d))


# In[36]:


delaybeam=c*ar*0.000001/(d*bw)  #arcseconds
print("delaybeam {0:9.1f} arccec".format(delaybeam))
dd=delaybeam/3600.
print("or {dd:5.3f}deg".format(dd=dd))


# If field size is $\theta$ basline B wavelength $\lambda$  then the maximum difference in fringe rate (Hz) and there are DAY seconds per day
# 
# $df = \frac{B}{\lambda} \theta \frac{2\pi}{DAY}$
# 
# 

# In[20]:


theta=2*3600 #arcseonds
df=d*theta*2*m.pi*1e5/(lam*ar*day)
print ("Peak difference in fringe rate {0:5.3f} Hz".format(df))
#maximum integration time = quarter period
tmax=0.25/df
print ("Maximum integration time {0:5.1f}s".format(tmax))
"""
or the other way about

df=d*theta*2*m.pi*1e5/(lam*ar*day) = 0.25/tmax
"""

size= 0.25 *lam*ar*day/(d*2*m.pi*1e5*t)
print ("field size for no smearing at integration time {0:4.1f}s is {1:6.2f}deg".format(t,size/3600))


# In[21]:


delaybm2=61838/(d*bw)
print ("Delay beam estimates {0:6.2f} {1:6.2f} arcsec".format( delaybeam, delaybm2))


# In[22]:


wbig= m.sqrt(res/(ar)*m.pi)*ar
print (wbig, "Arcsec")


# In[23]:


print("Delay beam {0:6.2f}deg  and W significant at {1:6.2f}deg ".format(delaybeam/3600,wbig/3600))


# In[28]:


"""
Field size, averaging period
"""
field=2*3600            #2 degree
period= 7090*lam/(d*field)
print("Max averaging time {0:6.3f}s For 1/4 period of fringe beating".format(period))


# In[35]:


"""
Telescope diam, Tsys,Efficiency

"""
diam=13.5  #m
eff=0.9    #fractional efficiency
Tsys=20       #K
gain=diam*diam*0.00028*eff #K/Jy - uses various things like boltzmann constant, speed of light
sefd=Tsys/gain #Jy
ae_tsys = m.pi*diam*diam*eff/(4*Tsys)
print ("Gain {0:6.4f}K/Jy \t SEFD {1:6.1f}Jy\t Ae/Tsys {2:6.2f}K/m^2".       format(gain,sefd,ae_tsys))   # for a single dish


# In[30]:


"""
sensitivity per baseline, per integration, per bandwidth
"""
mjy=1.1*sefd/(m.sqrt(bw*t)) # in one integration per bandwidth
print("Sensitivity {0:6.2f}mJy".format(mjy))


# In[31]:


"""
array values
"""
nants=64

print("Gain = {0:6.2f}K/Jy  \tSEFD = {1:6.2f} \t  Ae/Tsys  {2:6.2f} \t Sensitivity per integration {3:6.4f}mJy ".format(gain*nants,sefd/nants, ae_tsys*nants, mjy/m.sqrt(nants*(nants-1)/2)))

