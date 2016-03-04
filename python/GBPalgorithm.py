#global back projection algorithm for the radar stuff.
#basically sets up a number of pixels and assigns values to them based on all the fft data from the period of time
#takes in frequency data, position of plane. Could happen in real time, doesn't have to though.
def GBP()
	#define pixel size and position
	#bottom lefthand corner of area of interest.
	blhc=[utm_northpoint, utmeastpoint]
	#size in WE direction	
	xsize=100 
	#size in NS direction
	ysize=100
	#pixels in x direction
	nx=200
	#pixels in y direction
	ny=200
	#fmax is highest frequency we could expect from the plane speed and frequency there is a proper way to determine this
	fmax=200
	#size of pixel
	pisx=xsize/nx
	pisy=ysize/ny
	

	#big important loop that does stuff
	#just like obviously not how python for loops work but whatever.

	#just pretend I have this information
	#frespec
	#utmnorth
	#utmeast
	#course
	#alt
	#speed
	#which corresponds to the same time as frespec
	for x=1:1:nx
		for y=1:1:ny
			xdist=
			ydsit=		




