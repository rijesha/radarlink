from time import clock, sleep, gmtime, strftime

import threading
import ivylinker
import mBEElinker
import processing
import mutex

mBEErunnerperiod = 1
processingrunnerperiod = .1
portname = '/dev/ttyS0'
baudrate = 115200


class main:

    def __init__(self):
        self.shutdown = False
        self.procinitialized = False
        self.initprocessing()
        self.initFile()
        self.initIVY()
        self.initmBEE()
        self.procTH = threading.Thread(target=self.proc.runner, args=[processingrunnerperiod])
        self.procTH.start()

    def initprocessing(self):
        self.proc = processing.processing()
        self.procinitialized = True

    def initFile(self):
        try:
            self.logfile = open("log_" + strftime("%Y-%m-%d %H:%M:%S" + ".log", gmtime()), 'a+')
            self.filewritelock = mutex.mutex()
        except:
            print("Failed to Initialize File")

    def initIVY(self):
        try:
            self.ivylink = ivylinker.CommandReader(verbose=True, callback=self.msg_handler)
        except:
            print("Failed to initialize ivylink")

    def initmBEE(self):
        self.mBEElink = mBEElinker.mBEEReader(portname, baudrate)

    def filewriter(self, msg):
        string = ""
        for item in msg:
            string = string + " " + str(item)
        self.logfile.write(string + "\n")
        self.filewritelock.unlock()

    def msg_handler(self, acid, msg):
        if (msg.name in ["GPS", "ATTITUDE", "ESTIMATOR"]):
            senttoproc = self.proc.newtelemetrymsg(msg) if self.procinitialized else 0
            self.filewritelock.lock(self.filewriter, [clock(), msg.to_dict()])

    def closeFile(self):
        self.logfile.close()

    def shutdown(self):
        # turns off mBEE link
        self.shutdown = True
        # truns off processing
        self.proc.shutdown = True
        self.closeFile()
        self.ivylink.__del__()

if __name__ == "__main__":
    main()
