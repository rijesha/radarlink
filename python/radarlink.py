from time import clock, sleep, gmtime, strftime

import threading
import ivylinker
import mBEElinker

mBEEcommandperiod = 1

class main:

    def __init__(self):
        self.shutdown = False
        self.writebusy = False
        self.initIVY()
        self.initFile()
        self.initmBEE()
        if self.mBEElink.linksucess == True:
            self.mBEETH = threading.Thread(target=self.mBEEhandler)
            self.mBEETH.start()

    def initFile(self):
        self.logfile = open("log_" + strftime("%Y-%m-%d %H:%M:%S", gmtime()), 'a+')

    def initIVY(self):
        print("Initializing ivylink")
        self.newmissionstatus = False
        self.lastmissionmsg = None
        self.lastgps = None
        self.lastattitude = None
        self.lastestimator = None
        self.telinfoavailable = False
        self.ivylink = ivylinker.CommandSender(
            verbose=True, callback=self.msg_handler)
        self.lastmissionmessagetime = clock()

    def initmBEE(self):
        print("Initializing mBEE")
        self.mBEElink = mBEElinker.mBEEReader()
        self.lastmBEEmsg = None
        self.mBEEinfoavailable = False

    def mBEEhandler(self, msg):
        while (self.shutdown=False):
            mBEEmsgwritten = True #change to false once msg code is enetered.
            # insert code here for read/write commands
            #           self.mBEElink.ser.write("command message")
            #           msg = self.mBEElink.ser.Readline()
            #           writetomaththread
            while (mBEEmsgwritten == False):
                if (self.writebusy == False):
                    self.writebusy = True
                    self.filewriter("mBEEmessage", msg)
                    self.writebusy = False
                    mBEEmsgwritten == True
            print("nothing is being read")
            pause(mBEEcommandperiod)
        self.mBEElink.__del__()

    def filewriter(self, name, msg):
        self.logfile.write(clock(), name + msg + "\n")

    def msg_handler(self, acid, msg):
        print("Telemetry message recieved")
        telmsgwritten = False
        if (msg.name == "GPS"):
            self.lastgps = msg

        if (msg.name == "ATTITUDE"):
            self.lastattitude = msg

        if (msg.name == "ESTIMATOR"):
            self.lastestimator = msg

        if (self.lastgps != None) and (self.lastattitude != None) and (self.lastestimator != None):
            self.telinfoavailable = True

        while (telmsgwritten == False):
            if (self.writebusy == False):
                self.writebusy = True
                self.filewriter(msg.name, msg.fieldvalues)
                self.writebusy = False
                telmsgwritten == True


    def closeFile(self):
        self.logfile.close()

    def shutdown(self):
        self.shutdown = True  # turns off mBEE link
        self.closeFile()
        self.ivylink.__del__()
