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
        self.radarmutex.lock(self.radarmsg, msg)
        self.radarmsg = True

    def radarmsg(self, msg=None):
        if msg != None:
            self.I = msg[0]
           # self.Q = msg[1]
           # self.FFT = msg[2]
        elif msg == None:
            self.lastI = self.I
<<<<<<< HEAD
           # self.lastQ = self.Q
           # self.lastFFT = self.FFT
=======
            self.lastQ = self.Q
            self.lastFFT = self.FFT
            self.radaravail.set()
>>>>>>> 49ae7877f556c155596ad5cf63a4f196b16a818c
        self.radarmutex.unlock()








    def runner(self, period, radarenable):
<<<<<<< HEAD
        print("waiting for first telemetry message......")

=======
>>>>>>> 49ae7877f556c155596ad5cf63a4f196b16a818c

        if radarenable == True:
            print("waiting for first radar message.......")
            while (self.radarmsgavailable != False):
                if self.shutdown == True:
                    break
                sleep(.1)
            print("Found Radar message")
        else:
            print("processing without radarmsg")




        print("waiting for first telemetry message......")
        while (self.gps == None or self.est == None or self.att == None):
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


            if radarenable == True:
                self.radarmutex.lock(self.radarmsg, None)
<<<<<<< HEAD
		sleep(2)
                plt.plot(self.lastI) #plot fft
=======
                self.radaravail.wait()
                plt.plot(lastFFT) #plot fft
>>>>>>> 49ae7877f556c155596ad5cf63a4f196b16a818c
                plt.show()

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
