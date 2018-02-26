/* *************************************************************
   Encoder definitions

   Add an "#ifdef" block to this file to include support for
   a particular encoder board or library. Then add the appropriate
   #define near the top of the main ROSArduinoBridge.ino file.

   ************************************************************ */

#ifdef USE_BASE

#ifdef ROBOGAIA
/* The Robogaia Mega Encoder shield */
//#include "MegaEncoderCounter.h"

/* Create the encoder shield object */
MegaEncoderCounter encoders = MegaEncoderCounter(4); // Initializes the Mega Encoder Counter in the 4X Count modee

/* Wrap the encoder reading function */
long readEncoder(int i) {
  if (i == LEFT) return encoders.YAxisGetCount();
  else return encoders.XAxisGetCount();
}

/* Wrap the encoder reset function */
void resetEncoder(int i) {
  if (i == LEFT) return encoders.YAxisReset();
  else return encoders.XAxisReset();
}
#elif defined(ARDUINO_ENC_COUNTER)

volatile int leftPulses = 0;
volatile int rightPulses = 0;


void leftcount() {
  // This function is called by the interrupt
  // If leftDirection is HIGH decrement the counter
  // otherwise increment it
  if (!digitalRead(A2)) {
    leftPulses--;
    //rightPulses=leftPulses;
    //leftPulses=rightPulses;
  }
  else {
    leftPulses++;
    //rightPulses=leftPulses;
    //leftPulses=rightPulses;
  }

  /* Serial.print("leftPulses: ");
    Serial.print(leftPulses);
    Serial.print('\n');
    //Serial.println(motorDriver.getM2CurrentMilliamps());
    //Serial.println("current for M1"+motorDriver.getM1CurrentMilliamps());*/
}
void rightcount() {
  // This function is called by the interrupt
  // If rightDirection is HIGH decrement the counter
  // otherwise increment it

  if (digitalRead(A4)) {
    rightPulses--;
    //leftPulses=rightPulses;
    //rightPulses=leftPulses;
  }
  else {
    rightPulses++;
    //leftPulses=rightPulses;
    //rightPulses=leftPulses;
  }
  /*Serial.print("rightPulses: ");
    Serial.print(rightPulses);
    Serial.print('\n');
    //Serial.println(motorDriver.getM1CurrentMilliamps());*/



}

int correctError(int count, int rightMotorSpeed) {

  float errorAtFifty = 45.39550745;
  float errorAt100 = 12.3081882;
  float errorAt200 = 6.474063879;
  float errorAt300 = 5.86772637;
  float errorAt400 = 4.001936107;

  float fiftyToHundredper1 = 0.661746385;
  float hundredToTwoHundredper1 = 0.058341243;
  float TwoHundredToThreeHundredper1 = 0.006063375;
  float ThreeHundredToFourHundredper1 = 0.018657903;

  if (rightMotorSpeed >= 50 & rightMotorSpeed < 100) {
    int difference = rightMotorSpeed - 50;
    printf("%i\n", difference);
    float multiplyError = errorAtFifty - difference * fiftyToHundredper1;
    printf("%f\n", multiplyError);
    float count1 = count + count * (multiplyError / 100);
    int count2 = (int)(count1 + 0.5);
    printf("%i\n", count2);
    return count;
  }
  if (rightMotorSpeed >= 100 & rightMotorSpeed < 200) {
    int difference = rightMotorSpeed - 100;
    float multiplyError = errorAt100 - difference * hundredToTwoHundredper1;
    int count1 = count + count * (multiplyError / 100);
    int count2 = (int)(count1 + 0.5);
    printf("%i\n", count2);
    return count;
  }
  if (rightMotorSpeed >= 200 & rightMotorSpeed < 300) {
    int difference = rightMotorSpeed - 200;
    float multiplyError = errorAtFifty - difference * TwoHundredToThreeHundredper1;
    int count1 = count + count * (multiplyError / 100);
    int count2 = (int)(count1 + 0.5);
    printf("%i\n", count2);
    return count;
  }
  if (rightMotorSpeed >= 300 & rightMotorSpeed <= 400) {
    int difference = rightMotorSpeed - 300;
    float multiplyError = errorAtFifty - difference * ThreeHundredToFourHundredper1;
    int count1 = count + count * (multiplyError / 100);
    int count2 = (int)(count1 + 0.5);
    printf("%i\n", count2);
    return count;
  }
}

/* Wrap the encoder reading function */
long readEncoder(int i) {
  if (i == LEFT) return leftPulses;
  else return rightPulses;
}

/* Wrap the encoder reset function */
void resetEncoder(int i) {
  if (i == LEFT) {
    leftPulses = 0;
    return;
  } else {
    rightPulses = 0;
    return;
  }
}
#else
#error A encoder driver must be selected!
#endif

/* Wrap the encoder reset function */
void resetEncoders() {
  resetEncoder(LEFT);
  resetEncoder(RIGHT);
}

#endif

