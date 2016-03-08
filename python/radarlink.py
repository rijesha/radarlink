from time import clock, sleep, gmtime, strftime

import threading
import ivylinker
import mBEElinker
import processing

mBEEcommandperiod = 1

class main:

    def __init__(self):
        self.shutdown = False
        self.filewritebusy = False
        self.initprocessing()
        self.initIVY()
        self.initFile()
        self.initmBEE()
        #self.procTH = threading.Thread(target=self.proc.runner)
        #sleep(3)
        #self.procTH.start()


    def initprocessing(self):
        self.proc = processing.processing()

    def initFile(self):
        self.logfile = open("log_" + strftime("%Y-%m-%d %H:%M:%S", gmtime()), 'a+')

    def initIVY(self):
        print("Initializing ivylink")
        self.ivylink = ivylinker.CommandReader(
            verbose=True, callback=self.msg_handler)

    def initmBEE(self):
        print("Initializing mBEE")
        self.mBEElink = mBEElinker.mBEEReader()

    def filewriter(self, cputime, name, msg):
        string = str(cputime) + " " + str(name) + " " + str(msg);
        self.logfile.write(string + "\n")

    def msg_handler(self, acid, msg):
        #print("Telemetry message recieved")
        telmsgwritten = True
	print(msg.name)
        if (msg.name == "GPS"):
            print(msg.name)
            self.proc.newgpshandler(msg)
            telmsgwritten = False

        if (msg.name == "ATTITUDE"):
            self.proc.newattitudehandler(msg)
            telmsgwritten = False

        if (msg.name == "ESTIMATOR"):
            print(msg.name)
            self.proc.newestimatorhandler(msg)
            telmsgwritten = False

        while (telmsgwritten == False):
            if (self.filewritebusy == False):
                self.filewritebusy = True
                self.filewriter(clock(), msg.name, msg)
                self.filewritebusy = False
                telmsgwritten == True

    def closeFile(self):
        self.logfile.close()

    def shutdown(self):
        self.shutdown = True  # turns off mBEE link
        self.proc.shutdown = True # truns off processing
        self.closeFile()
        self.ivylink.__del__()

if __name__ == "__main__":
    main()
