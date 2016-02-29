def place_from_detect(centobjdet)
	
	




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


def line_from_vrel( vrel, 
	return


def mainfreq(frespec)
	#a=np.arrange().reshape(,)
	#
	#
	top=np.amax(frespec) 
	#hopefully returns max value
	mainfreq=np.argmax(frespec)
	#hopefully returns frequency of peak value.








