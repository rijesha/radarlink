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
			xdist=nx+blhc(2)-utmeast
			ydsit=ny+blhc(1)-utmnorth		
			h=sqrt(xdist^2+ydist^2)			
			alpha=numpy.atan(ydist/xdist)
			coursedeg=course*pi*180			
			Beta=coursedeg-alpha			
			fordir=h*numpy.cos(Beta)
			siddir=h*numpy.sin(Beta)
			vx=
			vy=
			vref=(vx*xdist+vy*ydist)/(math.sqrt(xdist**2 +ydist**2 +9))
			freq=fradar*((c+vref)/(c-vref))
			
					
				
				
				
				
			
			
				

			


