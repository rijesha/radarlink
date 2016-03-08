import serial

class mBEEReader(object):
    def __init__(self, callback = None):
        self.callback = callback
        try:
            self.ser = serial.Serial('/dev/ttyS0',115200)
            self.ser.open()
            self.linksuccess = self.ser.isOpen
        except:
            self.linksuccess = False


    def runner(self):
        while (self.shutdown == False):
# insert code here for read/write commands
            print("nothing is being read")
#       ser.write and ser.Readline
#        self.callback(receiveddata)


    def message_recv(self, ac_id, msg):
        if (self.callback != None):
            self.callback(ac_id, msg)

    def shutdown(self):
        print("Shutting down serial interface...")
        self.ser.close()

    def __del__(self):
        self.shutdown()

    def bramread(blockname, datapoints):
        data = []
        for i=0:datapoints-1:
            ser.writeLine('bramread' + blockname + str(i))
            data = [data ser.readline()]

        #convert into unsigned into
        for i=1:datapoints:
            data[i] = int(data[i],2)
