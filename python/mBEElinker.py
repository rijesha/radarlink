import serial


class mBEEReader(object):

    def __init__(self, portname, baudrate):
        try:
            self.ser = serial.Serial(portname, baudrate)
            self.ser.open()
            self.linksuccess = self.ser.isOpen
        except:
            self.linksuccess = False
            print("failed to open mBEE link")


    def shutdown(self):
        print("Shutting down serial interface...")
        self.ser.close()

    def __del__(self):
        self.shutdown()

    def bramread(blockname, datapoints):
        data = []
        for i in range(0, (datapoints - 1)):
            ser.writeLine('bramread' + blockname + str(i))
            data = [data, ser.readline()]
        # convert into unsigned into
        for i in range(1, datapoints):
            data[i] = int(data[i], 2)
