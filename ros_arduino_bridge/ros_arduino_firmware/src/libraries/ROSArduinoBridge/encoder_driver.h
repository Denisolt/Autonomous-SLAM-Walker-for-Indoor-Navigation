/* *************************************************************
   Encoder driver function definitions - by James Nugen
   ************************************************************ */
   
   
#ifdef ARDUINO_ENC_COUNTER
  //below can be changed, but should be PORTD pins; 
  //otherwise additional changes in the code are required
  #define leftCounter PC3  //pin 2
  #define leftDirection PC2  //pin 3
  
  //below can be changed, but should be PORTC pins
  #define rightCounter PC5  //pin A4
  #define rightDirection PC4   //pin A5
#endif
   
long readEncoder(int i);
void resetEncoder(int i);
void resetEncoders();

