import serial

class mBEEReader(object):
    def __init__(self, callback = None):
        self.callback = callback
        self.ser = serial.Serial('/dev/ttyS0',115200)
        self.ser.open()
        self.linksucess = self.ser.isOpen

    def runner(self)
        while (self.shutdown = False):
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
