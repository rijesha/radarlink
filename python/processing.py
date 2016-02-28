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
            print("running the processing loop")
            sleep(1)
        print("shutting down the processing loop")
