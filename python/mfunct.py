import numpy
import scipy

def detfmovavg(frag)
	#trying to detect from moving average
	#frag is a small piece of the freq. spctrum
	eps=0.01	
	su=numpy.sum(frag)
	re=numpy.size(frag)
	t=round(re/2.0)
	y=frag[t]
	compare=su/re+eps
	if(y>compare)
		ret=1
	else
		ret=0
	return ret



def detfmdervi(frag)
	# takes in piece of frequency spectrum
	#trying to detect from derivative
	siz=numpy.size(frag)
	for index in range(len(frag)-1)
		myarr[index]=frag[index+1]-frag[index]
	mybool=detfmovavg(myarr)		
	return	mybool
	

def obj_detec(frespec)
	

	favg=frespec[i]+frespec[i+1]+frespec[i+2]


def vrel_from_freq(fobj)
	#takes in the frequency of the object
	#and converts it into the relative velocity
	#of the object that was detected.
	fdbb=3000000000.0 # change this.
	#frequency of minibee LO
	fvco=2400000000.0
	#frequency of PCB LO
	fradar=900000000.0
	#frequency of 900 MHz thing
	x=(fobj+fdbb-fvco)/fradar
	c=300000000.0
	vrel=c*(x-1.0)/(x+1.0)

	if abs(vrel)>30.0 : print "vrel seems really high"
		
	return vrel


def line_from_vrel( vrel)
	
	return


def mainfreq(frespec)
	#returns tuple of the max value and 
	#the frequency of that max value.
	#a=numpy.arrange().reshape(,)
	#1 line extra
	#
	top=numpy.amax(frespec) 
	#hopefully returns max value
	mainfreq=numpy.argmax(frespec)
	#hopefully returns frequency of peak value.
	return (top,mainfreq)










