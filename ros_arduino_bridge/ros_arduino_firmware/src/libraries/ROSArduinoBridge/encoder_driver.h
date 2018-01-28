/* *************************************************************
   Encoder driver function definitions - by James Nugen
   ************************************************************ */
   
   
#ifdef ARDUINO_ENC_COUNTER
  //below can be changed, but should be PORTD pins; 
  //otherwise additional changes in the code are required
  #define leftCounter PD0  //DT pin on the KY-040 (yellow)
  #define leftClk PD1  //CLK pin on the KY-040 (green)
  
  //below can be changed, but should be PORTC pins
  #define rightCounter PD5  //pin A4 (yellow)
  #define rightClk PD3  //pin A5 (green)
#endif
   
long readEncoder(int i);
void resetEncoder(int i);
void resetEncoders();

