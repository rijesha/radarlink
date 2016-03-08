import mfunct
import scipy.io
import scipy

mydict={}
scipy.io.loadmat("frequencies.mat",mydict)
#define some test varialbles
utmeast=37482848 #cm
utmnorth=422292896
course=289 #decieegree
zone=18
alt=4246 #mm actually 12m rest is error. 
altalt=9.43 #meters above ground
speed=38 #cm/s
itow=564923400
freqspectrum=
wrapper(utmeast,utmnorth, course, alt, speed, zone, altalt,itow,freqspectrum)
print "hey" 
