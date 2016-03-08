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
            utmnorth = self.lastgpsmsg.utm_north
            course = self.lastgpsmsg.course
            alt = self.lastgpsmsg.alt
            speed = self.lastgpsmsg.speed
            zone = self.lastgpsmsg.utm_zone
            print(self.lastestimator)
            print(self.lastestimator.z)
            altalt = self.lastestimator.z
            itow = self.lastgpsmsg.itow
            print(utmeast)
            print(itow)
            print(zone)
            print("running the processing loop")
            sleep(1)
        print("shutting down the processing loop")
