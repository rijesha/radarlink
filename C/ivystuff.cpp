#include <glib.h>
#include <stdio.h>
#include <stdlib.h>

#include <Ivy/ivy.h>
#include <Ivy/ivyglibloop.h>

void on_Estimator(IvyClientPtr app, void *user_data, int argc, char *argv[]){
  int32_t alt,
  alt = atoi(argv[1])
  printf("Yolo SWAG\n", );

}


void on_GPS(IvyClientPtr app, void *user_data, int argc, char *argv[]){
/*
    <message name="GPS" id="8">
      <field name="mode"       type="uint8"  unit="byte_mask"/>
      <field name="utm_east"   type="int32"  unit="cm" alt_unit="m"/>
      <field name="utm_north"  type="int32"  unit="cm" alt_unit="m"/>
      <field name="course"     type="int16"  unit="decideg" alt_unit="deg"/>
      <field name="alt"        type="int32"  unit="cm" alt_unit="m"/>
      <field name="speed"      type="uint16" unit="cm/s" alt_unit="m/s"/>
      <field name="climb"      type="int16"  unit="cm/s" alt_unit="m/s"/>
      <field name="week"       type="uint16" unit="weeks"></field>
      <field name="itow"       type="uint32" unit="ms"/>
      <field name="utm_zone"   type="uint8"/>
      <field name="gps_nb_err" type="uint8"/>
    </message>
*/

   int32_t alt, utm_east, utm_north;
   int16_t course, speed;

   utm_east = atoi(argv[2]) / 100;
   utm_west = atoi(argv[3]) / 100;
   course = atoi(argv[4]);
   speed = atoi(argv[6]) / 100;
   alt = atoi(argv[5]) / 100;

 }
