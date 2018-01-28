#ifdef USE_BASE

#ifdef ROBOGAIA
/* The Robogaia Mega Encoder shield */
#include "MegaEncoderCounter.h"

/* Create the encoder shield object */
MegaEncoderCounter encoders = MegaEncoderCounter(4); // Initializes the Mega Encoder Counter in the 4X Count mode

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

volatile int leftPosCounter = 0; //keeps track of the ticks of left encoder
volatile int rightPosCounter = 0; //keeps track of the ticks of right encoder
volatile int pinLeftClkLast; ////keeps track of the last tick of left encoder
volatile int pinRightClkLast; ////keeps track of the last tick of left encoder
volatile int leftVal;
volatile int rightVal;

void leftcount() {
  leftVal = digitalRead(leftClk);
  if (leftVal != pinLeftClkLast) { // Means the knob is rotating
    // if the knob is rotating, we need to determine direction
    // We do that by reading pin B.
    if (digitalRead(leftCounter) != leftVal) {  // Means pin A Changed first - We're Rotating Clockwise
      leftPosCounter ++;
    }
    else {// Otherwise B changed first and we're moving CCW
      leftPosCounter--;
    }
    pinLeftClkLast = leftVal;
  }
}


void rightcount() {
  rightVal = digitalRead(rightClk);
  if (rightVal != pinRightClkLast) { // Means the knob is rotating
    // if the knob is rotating, we need to determine direction
    // We do that by reading pin B.
    if (digitalRead(rightCounter) != rightVal) {  // Means pin A Changed first - We're Rotating Clockwise
      rightPosCounter ++;
    }
    else {// Otherwise B changed first and we're moving CCW
      rightPosCounter--;
    }
    pinRightClkLast = rightVal;
  }
}

/* Wrap the encoder reading function */
long readEncoder(int i) {
  if (i == LEFT) return leftPosCounter;
  else return rightPosCounter;
}

/* Wrap the encoder reset function */
void resetEncoder(int i) {
  if (i == LEFT) {
    leftPosCounter = 0;
    return;
  } else {
    rightPosCounter = 0;
    return;
  }
}
#else

#endif

/* Wrap the encoder reset function */
void resetEncoders() {
  resetEncoder(LEFT);
  resetEncoder(RIGHT);
}

#endif
