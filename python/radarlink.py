from time import clock, sleep, gmtime, strftime

import threading
import ivylinker
import mBEElinker
import processing
import mutex

mBEEcommandperiod = 1


class main:

    def __init__(self):
        self.shutdown = False
        self.procinitialized = False
        self.initprocessing()
        self.initFile()
        self.initIVY()
#        self.initmBEE()
        #self.procTH = threading.Thread(target=self.proc.runner)
        # sleep(3)
        # self.procTH.start()

    def initprocessing(self):
        self.proc = processing.processing()
        self.procinitialized = True

    def initFile(self):
        self.logfile = open(
            "log_" + strftime("%Y-%m-%d %H:%M:%S" + ".log", gmtime()), 'a+')
        print("making a new file")
        self.filewritelock = mutex.mutex()
        print("finished making a new file")

    def initIVY(self):
        print("Initializing ivylink")
        self.ivylink = ivylinker.CommandReader(
            verbose=True, callback=self.msg_handler)

    def initmBEE(self):
        print("Initializing mBEE")
        self.mBEElink = mBEElinker.mBEEReader()

    def filewriter(self, msg):
        string = ""
        for item in msg:
            string = string + " " + str(item)
        self.logfile.write(string + "\n")
#        print("writing string ____________________")
#        print(string)
        self.filewritelock.unlock()

    def msg_handler(self, acid, msg):
        writemsg =False
        if (msg.name == "GPS"):
#            self.proc.newgpshandler(msg)
            writemsg = True

        if (msg.name == "ATTITUDE"):
#            self.proc.newattitudehandler(msg)
            writemsg = True

        if (msg.name == "ESTIMATOR"):
#            self.proc.newestimatorhandler(msg)
            writemsg = True

        if writemsg == True:
            senttoproc = self.proc.newtelemetrymsg(msg) if self.procinitialized else 0
            self.filewritelock.lock(self.filewriter,[clock(), msg.name, msg])


    def closeFile(self):
        self.logfile.close()

    def shutdown(self):
        self.shutdown = True  # turns off mBEE link
        self.proc.shutdown = True  # truns off processing
        self.closeFile()
        self.ivylink.__del__()

if __name__ == "__main__":
    main()
