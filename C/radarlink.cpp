#include <glib.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <thread>

#include <Ivy/ivy.h>
#include <Ivy/ivyglibloop.h>
#include <processing.h>

using namespace std;

class radarlink {
private:

  bool shutdown      = FALSE;
  bool filewritebusy = FALSE;
  ofstream logfile;
  processing proc;
  thread procTH(proc.runner);


  void initFile(void)
  {
    logfile.open("log.txt");
  }

  void filewriter(msg)
  {
    bool filewritten = FALSE;
    while (filewritten ==FALSE)
    {
      if (filewritebusy == FALSE)
      {
        filewritebusy = TRUE;
        //strprint function
        logfile << "Writing this to a file.\n";
        filewritebusy = FALSE;
      }
      filewritten = TRUE;
    }

  }

  void closefile(void)
  {
    logfile.close();
  }

  void IVYrunner(void)
  {
    GMainLoop *ml = g_main_loop_new(NULL, FALSE);

    IvyInit("RadarReader", "Radar READY", NULL, NULL, NULL, NULL);
    IvyBindMsg(on_GPS, NULL, "^(\\S*) GPS (\\S*) (\\S*) (\\S*) (\\S*) (\\S*) (\\S*) (\\S*) (\\S*) (\\S*) (\\S*) (\\S*)");
    IvyBindMsg(on_Estimator, NULL, "^(\\S*) GPS (\\S*) (\\S*) (\\S*)");
    IvyStart("127.255.255.255");
    print("Initializing ivylink");

    g_main_loop_run(ml);
  }

  void on_Estimator(IvyClientPtr app, void *user_data, int argc, char *argv[])
  {
    estmsgstruct estmsg;
    estmsg.alt = atoi(argv[1]);
    filewriter(estmsg);
    proc.newest(estmsg);
  }

  void on_GPS(IvyClientPtr app, void *user_data, int argc, char *argv[])
  {

    gpsmsgstruct gpsmsg;
    gpsmsg.utm_east = atoi(argv[2]) / 100;
    gpsmsg.utm_west = atoi(argv[3]) / 100;
    gpsmsg.course   = atoi(argv[4]);
    gpsmsg.speed    = atoi(argv[6]) / 100;
    gpsmsg.alt      = atoi(argv[5]) / 100;

    filewriter(gpsmsg); //need to write code for this with time
    proc.newgps(gpsmsg);

    printf("GPS message\n", );
  }


void shutdown(void)
{
  closefile();

}


public:

  void radarlink(void)
  {
    initFile();
    IVYrunner(); //Put into a thread

    procTH.join(); //  have as last thread
    shutdown();
//    initmBEE();
  }
};

/*

*
 * void initmBEE(void){
 * print("Initializing mBEE")
 * self.mBEElink = mBEElinker.mBEEReader()
 * self.lastmBEEmsg = None
 * self.mBEEinfoavailable = False
 }


 * void mBEEhandler(self, msg){
 *      while (self.shutdown=False):
 *          mBEEmsgwritten = True #change to false once msg code is enetered.
 # insert code here for read/write commands
 #           self.mBEElink.ser.write("command message")
 #           msg = self.mBEElink.ser.Readline()
 #           writetomaththread
 #          while (mBEEmsgwritten == False):
 #              if (self.filewritebusy == False):
 #                  self.filewritebusy = True
 #                  self.filewriter("mBEEmessage", msg)
 #                  self.filewritebusy = False
 #                  mBEEmsgwritten == True
 #          print("nothing is being read")
 #          sleep(mBEEcommandperiod)
 #      self.mBEElink.__del__()
 # }
 #
*/
