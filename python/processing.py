from time import sleep
from mutex import mutex


class processing:

    def __init__(self):
        print('intiailizing processing')
        self.gpsmutex = mutex()
        self.estmutex = mutex()
        self.attmutex = mutex()
        self.att = None
        self.est = None
        self.gps = None
        self.lastatt = None
        self.lastest = None
        self.lastgps = None
        self.lastradar = None
        self.shutdown = False

    def newtelemetrymsg(self, msg):
        if msg.name == "ESTIMATOR":
            self.estmutex.lock(self.estmsg, msg)
        elif msg.name == "GPS":
            self.gpsmutex.lock(self.gpsmsg, msg)
        elif msg.name == "ATTITUDE":
            self.attmutex.lock(self.attmsg, msg)
        return True

    def estmsg(self, msg=None):
        if msg != None:
            self.est = msg
        elif msg == None:
            self.lastest = est
        self.estmutex.unlock()

    def gpsmsg(self, msg=None):
        if msg != None:
            self.gps = msg
        elif msg == None:
            self.lastgps = self.gps
        self.gpsmutex.unlock()

    def attmsg(self, msg=None):
        if msg != None:
            self.att = msg
        elif msg == None:
            self.lastatt = self.att
        self.attmutex.unlock()



    def newmBEEhandler(self, msg):
        self.lastradar = msg

    def bindserialandfile(self, mbserial, logfile):
        self.serial = mbserserial
        self.logfile = logfile

    def getdata(void):
        # self.logfile.writeline(stuff)
        print("insert serial get stuff")
        self.lastrar = self.logfile.readline(stuff)



    def runner(self):
        while (self.shutdown == False):

            #these functions will update last***msg with the current msg
            self.gpsmutex.lock(self.gpsmsg, None)
            self.attmutex.lock(self.attmsg, None)
            self.estmutex.lock(self.estmsg, None)

            # getdata
            utmeast = self.lastgps.utm_north
            # meters east of point
            utmnorth = self.lastgps.utm_north
            # meters north of point
            course = float(self.lastgps.course)/10
            # angle of traveling
            # unit of degree
            alt = self.lastgps.alt
            # altitude above sea level?? meters.
            speed = self.lastgps.speed
            # speed m/s not velocity
            zone = self.lastgps.utm_zone
            # defines point which utm_east, utm_north are
            # relative too.
            altalt = self.lastest.z
            # alternative altitude estimator (more accurate)?
            itow = self.lastgps.itow
            # time not sure what format.
            print(utmeast)
            print(itow)
            print(course)
            print("running the processing loop")
          # wrapper(utmeast,utmnorth, course, alt, speed, zone, altalt,itow)
          # #not sure what this is??

            sleep(1)
        print("shutting down the processing loop")
