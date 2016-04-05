from time import sleep
from mutex import mutex
import matplotlib.pyplot as plt
import threading


class processing:

    def __init__(self):
        print('intiailizing processing')
        self.gpsmutex = mutex()
        self.estmutex = mutex()
        self.attmutex = mutex()
        self.radarmutex = mutex()
        self.radarmsgavailable = False
        self.gpsavail = threading.Event()
        self.estavail = threading.Event()
        self.attavail = threading.Event()
        self.radarupdate = threading.Event()
        self.att = None
        self.est = None
        self.gps = None
        self.lastatt = None
        self.lastest = None
        self.lastgps = None
        self.I = None
        self.lastI = None
        self.radarmsgavailable = False
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
            self.lastest = self.est
            self.estavail.set()
        self.estmutex.unlock()

    def gpsmsg(self, msg=None):
        if msg != None:
            self.gps = msg
        elif msg == None:
            self.lastgps = self.gps
            self.gpsavail.set()
        self.gpsmutex.unlock()

    def attmsg(self, msg=None):
        if msg != None:
            self.att = msg
        elif msg == None:
            self.lastatt = self.att
            self.attavail.set()
        self.attmutex.unlock()

    def newradarmsg(self, msg):
    #    print("received new radar")
        self.radarmutex.lock(self.radarmsg, [msg])
        if self.radarmsgavailable == False:
            sleep(.2)
            self.radarmsgavailable = True

    def radarmsg(self, msg=None):
        if msg != None:
       #     print(msg[0])
            self.I = msg[0]
    #        print("wrote to I")
        elif msg == None:
            self.lastI = self.I
            self.radarupdate.set()
        self.radarmutex.unlock()


    def runner(self, period, radarenable):

        if radarenable == True:
            print("waiting for first radar message.......")
            while (self.radarmsgavailable != False):
                print("waiting for radar message")
                if self.shutdown == True:
                    break
                sleep(.1)
            print("Found Radar message")
        else:
            print("processing without radarmsg")


        print("waiting for first telemetry message......")
        while (self.gps == None or self.est == None or self.att == None):
           # print("still waiting")
            if self.shutdown == True:
                break
            sleep(.1)
        if self.shutdown == True:
            print("shutting down processing loop")
            return 0
        print("all telemetry messages found")

        
        while (self.shutdown == False):

            # these functions will update last***msg with the current msg
            self.gpsmutex.lock(self.gpsmsg, None)
            self.gpsavail.wait()
            self.attmutex.lock(self.attmsg, None)
            self.attavail.wait()
            self.estmutex.lock(self.estmsg, None)
            self.estavail.wait()
            sleep(1)
            
            
            if radarenable == True:
                self.radarmutex.lock(self.radarmsg, None)
                self.radarupdate.wait()
                print("New Radar MSG in Proc Loop")
          #      print(self.lastI)
       #         plt.plot(self.lastI) #plot fft
    #            plt.show()

            # getdata
            utmeast = self.lastgps.utm_north
            # meters east of point
            utmnorth = self.lastgps.utm_north
            # meters north of point
            course = float(self.lastgps.course) / 10
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
    #        print(utmeast)
    #        print(itow)
            print(course)
          # wrapper(utmeast,utmnorth, course, alt, speed, zone, altalt,itow)
          # #not sure what this is??
            sleep(.05)
        print("shutting down the processing loop")
