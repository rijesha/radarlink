struct gpsmsgstruct
{
  int32_t alt, utm_east, utm_north;
  int16_t course, speed;
}

struct estmsgstruct
{
  int32_t alt;
}


class processing{
private:
  void initializevariables(void);
public:
  void processing(void);
  void runner(void);
  void newest(estmsgstruct estmsg);
  void newgps(gpsmsgstruc gpsmsg);
}
