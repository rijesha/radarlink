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
        data = [0] * (datapoints -1)
        self.ser.write('bramdump ' + blockname +' '  + str(datapoints) + '\r')
        time.sleep(.1)
        t1 = os.times()[4]

        for i in range(0, (datapoints - 1)):
            data[i] = self.ser.readline()

        print("read " + str(blockname) + " in " + str(os.times()[4] - t1) + " seconds" )

        for i in range(1, datapoints-1):
            h = data[i]
            data[i] = h[len(h)-6 :len(h)-1]

