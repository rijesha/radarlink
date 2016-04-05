import serial
import os
import time


class mBEEReader(object):

    def __init__(self, portname, baudrate):
        try:
            self.ser = serial.Serial(portname, baudrate)
            self.linksuccess = self.ser.isOpen()
        except:
            self.linksuccess = False
            print(self.linksuccess)
            print("failed to open mBEE link")


    def shutdown(self):
        print("Shutting down serial interface...")
        self.ser.close()

    def __del__(self):
        self.shutdown()

    def bramread(self, blockname, datapoints):
        self.data = []
        self.ser.write('bramdumpvalue ' + blockname +' '  + str(datapoints) + '\r')
        time.sleep(.1)
        t1 = os.times()[4]
        print(self.ser.readline())


        self.num = 0
        for self.num in range(0, datapoints-1):
            line = self.ser.readline()
            self.num = self.num+1            
            if line:
                self.data.append(line)
            if not line or line[-1:] != '\n':
                break
        print("read " + str(blockname) + " in " + str(os.times()[4] - t1) + " seconds" )

        return self.data

