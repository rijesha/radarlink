from time import sleep


class processing:

    def __init__(self):
        print('intiailizing processing')
        self.lastattitude = None
        self.lastestimator = None
        self.lastgps = None
        self.lastradar = None
        self.shutdown = False

    def newattitudehandler(self, msg):
        self.lastattitude = msg

    def newgpsehandler(self, msg):
        self.lastgps = msg

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
            utmeast = self.lastgpsmsg.fieldvalues[1]
            utmnorth = self.lastgpsmsg.fielvalues[2]
            course = self.lastgpsmsg.fieldvalues[3]
            alt = self.lastgpsmsg.fielvalues[4]
            speed = self.lastgpsmsg.fieldvalues[5]
            altalt = self.lastestimator.fieldvalues[1]
            zone = self.lastgpsmsg.fieldvalues[9]
            print("running the processing loop")
            sleep(1)
        print("shutting down the processing loop")
