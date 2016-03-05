from time import sleep


class processing:

    def __init__(self):
        print('intiailizing processing')
        self.lastattitude = None
        self.lastestimator = None
        self.lastgpsmsg = None
        self.lastradar = None
        self.shutdown = False

    def newattitudehandler(self, msg):
        self.lastattitude = msg

    def newgpshandler(self, msg):
        self.lastgpsmsg = msg

    def newestimatorhandler(self, msg):
        self.lastestimator = msg

    def newmBEEhandler(self, msg):
        self.lastradar = msg

    def bindserialandfile(self, mbserial, logfile):
        self.serial = mbserserial;
        self.logfile = logfile;

    def getdata(void):
        #self.logfile.writeline(stuff)
        print("insert serial get stuff")
        self.lastrar = self.logfile.readline(stuff)

    def runner(self):
        while (self.shutdown == False):
            #getdata
            utmeast = self.lastgpsmsg.utm_east
            #meters east of point            
            utmnorth = self.lastgpsmsg.utm_north
            #meters north of point            
            course = self.lastgpsmsg.course
            #angle of traveling, at instant?
            alt = self.lastgpsmsg.alt
            #altitude above sea level?? meters. 
            speed = self.lastgpsmsg.speed
            #speed m/s not velocity
            zone = self.lastgpsmsg.utm_zone
            #defines point which utm_east, utm_north are
            #relative too.           
            altalt = self.lastestimator.z
            #alternative altitude estimator (more accurate)?
            itow = self.lastgpsmsg.itow
            #time not sure what format. 
            print(utmeast)
            print(itow)
            print(zone)
            print("running the processing loop")
			wrapper(utmeast,utmnorth, course, alt, speed, zone, altalt,itow)    

		
            sleep(1)
        print("shutting down the processing loop")
