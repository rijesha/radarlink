from time import clock, sleep, gmtime, strftime

import threading
import ivylinker
import mBEElinker
import processing

mBEEcommandperiod = 1

class main:

    def __init__(self):
        self.shutdown = False
        self.writebusy = False
        self.initprocessing()
        self.initIVY()
        self.initFile()
        self.initmBEE()
        if self.mBEElink.linksucess == True:
            self.mBEETH = threading.Thread(target=self.mBEEhandler)
            self.mBEETH.start()
        self.procTH = threading.Thread(target=self.proc.runner)
        self.procTH.start()


    def initprocessing(self):
        self.proc = processing.processing()

    def initFile(self):
        self.logfile = open("log_" + strftime("%Y-%m-%d %H:%M:%S", gmtime()), 'a+')

    def initIVY(self):
        print("Initializing ivylink")
        self.ivylink = ivylinker.CommandSender(
            verbose=True, callback=self.msg_handler)

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
            sleep(mBEEcommandperiod)
        self.mBEElink.__del__()

    def filewriter(self, name, msg):
        self.logfile.write(clock(), name + msg + "\n")

    def msg_handler(self, acid, msg):
        print("Telemetry message recieved")
        telmsgwritten = True
        if (msg.name == "GPS"):
            self.proc.newgpshandler(msg)
            telmsgwritten = False

        if (msg.name == "ATTITUDE"):
            self.proc.newattitudehandler(msg)
            telmsgwritten = False

        if (msg.name == "ESTIMATOR"):
            self.proc.newestimatorhandler(msg)
            telmsgwritten = False

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
        self.proc.shutdown = True # truns off processing
        self.closeFile()
        self.ivylink.__del__()
