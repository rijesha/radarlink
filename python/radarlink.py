from time import clock, sleep, gmtime, strftime

import threading
import os
import signal
import ivylinker
import mBEElinker
import processing
import mutex

mBEErunnerperiod = 3
processingrunnerperiod = .1
portname = '/dev/ttyS0'
baudrate = 115200


class main:

    def __init__(self):
        self.shutdown = False
        signal.signal(signal.SIGINT, self.shutdownfunc)
        signal.signal(signal.SIGTERM, self.shutdownfunc)
        self.procinitialized = False
        self.initprocessing()
        self.initFile()
        self.initIVY()
        self.initmBEE()
        self.procTH = threading.Thread(target=self.proc.runner, args=[
                                       processingrunnerperiod, self.mBEElink.linksuccess])
        self.mBEETH = threading.Thread(target=self.mBEErunner)
        mBEErunning = self.mBEETH.start() if self.mBEElink.linksuccess else 0
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

    def mBEErunner(self):
        while (self.shutdown == False):
            ser.writeLineline('regwrite capture 1')
            capturetime = clock()
            ser.writeLineline('regwrite capture 0')
            sleep(2)
            I = bramread(ADC_RXI, 65536)
            Q = bramread(ADC_RXQ, 65536)
            FFT = bramread(fft, 65536)
            senttoproc = self.proc.newradarm([I, Q, FFT]) if self.procinitialized else 0
            self.filewritelock.lock(self.filewriter, [capturetime, I])
            self.filewritelock.lock(self.filewriter, [capturetime, Q])
            self.filewritelock.lock(self.filewriter, [capturetime, FFT])
            sleep(mBEErunnerperiod)
        print("shutdown mBEErunner")

    def closeFile(self):
        self.logfile.close()

    def shutdownfunc(self, signum, frame):
        self.shutdown = True
        self.proc.shutdown = True
        self.closeFile()
        self.ivylink.__del__()


if __name__ == "__main__":
    run = main()

    while True:
        if run.shutdown == True:
            break
        sleep(1)
