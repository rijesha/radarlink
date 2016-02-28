#include <processing.h>


class processing{
private:
  initializevariables(void){
    gpsmsgstruct lastgpsmsg;
    attmsgstruct lastattmsg;
    estmsgstruct lastestmsg;
  }

public:
  void processing(void){
    initializevariables(void);
  }
  void runner(void)
  {
    //Insert code for running everything.

  }
  void newest(estmsg)
  {
    lastestmsg = estmsg;
  }

  void newgps(gpsmsg)
  {
    lastgpsmsg = gpsmsg;
  }
}
